// Intersection Observer for Reveal Animations
const observerOptions = {
    threshold: 0.1
};

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            revealObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => {
    revealObserver.observe(el);
});

// Parallax effect for the Earth background (disabled on mobile for performance)
window.addEventListener('scroll', () => {
    if (window.innerWidth > 968) {
        const earth = document.getElementById('hero-earth');
        if (earth) {
            const scrolled = window.pageYOffset;
            earth.style.transform = `translateY(${-50 + scrolled * 0.1}%) translateX(${scrolled * 0.05}%)`;
        }
    }
});

// Mobile Menu Toggle Logic
const mobileToggle = document.getElementById('mobile-toggle');
const navLinks = document.getElementById('nav-links');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        mobileToggle.classList.toggle('active');
        navLinks.classList.toggle('active');

        // Prevent scrolling when menu is open
        if (navLinks.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'auto';
        }
    });

    // Close menu when clicking outside or on a link (if they were actual links)
    navLinks.addEventListener('click', (e) => {
        if (e.target.tagName === 'A' || e.target.closest('.search-icon')) {
            mobileToggle.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
}

// Simple Log to confirm script is running
console.log("National Geographic Theme Initialized - Design by Alterpix Inspiration");

/* === Search Logic for Explore Page === */
const searchBox = document.getElementById('search-box');
const cards = document.querySelectorAll('.material-card');
const noResults = document.getElementById('no-results');

if (searchBox) {
    searchBox.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        let matches = 0;

        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const tags = card.getAttribute('data-tags').toLowerCase();

            if (title.includes(query) || tags.includes(query)) {
                card.classList.remove('hidden');
                matches++;
            } else {
                card.classList.add('hidden');
            }
        });

        if (matches === 0 && query !== "") {
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
        }
    });
}