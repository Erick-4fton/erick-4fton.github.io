import os
import re
import html
import shutil

def convert_md_to_html():
    content_dir = 'content/'
    output_dir = 'pages/materials/' 
    template_path = 'templates/writeup-template.html'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # Bersihkan file lama
        for file in os.listdir(output_dir):
            if file.endswith('.html'):
                os.remove(os.path.join(output_dir, file))

    with open(template_path, 'r', encoding='utf-8') as f:
        original_template = f.read()

    # Get all materials first for the navigation list
    md_files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    all_materials = []

    for filename in md_files:
        with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            title = re.search(r'title: "(.*?)"', content).group(1) if re.search(r'title: "(.*?)"', content) else filename
            all_materials.append({
                'title': title,
                'url': filename.replace('.md', '.html')
            })

    # Sort materials alphabetically or you can add 'order' in frontmatter later
    all_materials.sort(key=lambda x: x['title'])

    # Process each file
    for filename in md_files:
        filepath = os.path.join(content_dir, filename)
        output_filename = filename.replace('.md', '.html')
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Metadata parsing
        title = re.search(r'title: "(.*?)"', md_content).group(1) if re.search(r'title: "(.*?)"', md_content) else "Untitled"
        date = re.search(r'date: (.*?)\n', md_content).group(1) if re.search(r'date: (.*?)\n', md_content) else ""
        category = re.search(r'category: "(.*?)"', md_content).group(1) if re.search(r'category: "(.*?)"', md_content) else "General"
        author = re.search(r'author: "(.*?)"', md_content).group(1) if re.search(r'author: "(.*?)"', md_content) else "Admin"

        # Generate Sidebar HTML
        sidebar_html = '<ul class="sidebar-list">'
        for item in all_materials:
            active_class = 'active' if item['url'] == output_filename else ''
            sidebar_html += f'<li class="{active_class}"><a href="{item["url"]}">{item["title"]}</a></li>'
        sidebar_html += '</ul>'

        # Body Processing
        body = re.sub(r'---.*?---', '', md_content, flags=re.DOTALL).strip()
        code_blocks = []
        def save_code(match):
            code_blocks.append(match.group(2))
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        body = re.sub(r'```(.*?)\n(.*?)```', save_code, body, flags=re.DOTALL)
        body = html.escape(body)

        # Markdown conversion
        body = re.sub(r'^# (.*)', r'<h1>\1</h1>', body, flags=re.MULTILINE)
        body = re.sub(r'^## (.*)', r'<h2>\1</h2>', body, flags=re.MULTILINE)
        body = re.sub(r'^### (.*)', r'<h3>\1</h3>', body, flags=re.MULTILINE)
        body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
        body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', body)
        body = re.sub(r'`(.*?)`', r'<code>\1</code>', body)
        body = re.sub(r'^> (.*)', r'<blockquote>\1</blockquote>', body, flags=re.MULTILINE)
        body = re.sub(r'^\d+\.\s+(.*)', r'<li>\1</li>', body, flags=re.MULTILINE)
        body = re.sub(r'-\s+(.*)', r'<li>\1</li>', body, flags=re.MULTILINE)
        body = re.sub(r'(<li>.*?</li>(?:\n<li>.*?</li>)*)', r'<ul>\1</ul>', body, flags=re.DOTALL)

        lines = body.split('\n')
        new_lines = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('<'):
                new_lines.append(f"<p>{line}</p>")
            else:
                new_lines.append(line)
        body = '\n'.join(new_lines)

        for i, code in enumerate(code_blocks):
            escaped_code = html.escape(code)
            body = body.replace(f"__CODE_BLOCK_{i}__", f'<pre><code>{escaped_code}</code></pre>')

        # Final Template Injection
        template = original_template.replace('href="../assets/', 'href="../../assets/')\
                                    .replace('src="../assets/', 'src="../../assets/')\
                                    .replace('href="../index.html"', 'href="../../index.html"')\
                                    .replace('href="../pages/explore.html"', 'href="../explore.html"')

        final_html = template.replace('{{ title }}', title)\
                             .replace('{{ date }}', date)\
                             .replace('{{ category }}', category)\
                             .replace('{{ author }}', author)\
                             .replace('{{ sidebar_nav }}', sidebar_html)\
                             .replace('{{ content }}', body)

        with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as f:
            f.write(final_html)
        
    print(f"Sukses! Build {len(md_files)} materi dengan navigasi.")

if __name__ == "__main__":
    convert_md_to_html()
