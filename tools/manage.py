import sys

def main():
    if len(sys.argv) < 2:
        print("Gunakan: python manage.py [new|rebuild|scan]")
        return

    cmd = sys.argv[1]
    if cmd == "new":
        print("Memasuki mode pembuatan post baru...")
    elif cmd == "rebuild":
        print("Membangun ulang seluruh website...")
    elif cmd == "scan":
        print("Menjalankan pemindaian keamanan...")
    else:
        print(f"Perintah '{cmd}' tidak dikenal.")

if __name__ == "__main__":
    main()
