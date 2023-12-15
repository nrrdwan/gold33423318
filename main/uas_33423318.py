from Librarymu.my_class import EmailFunctions
from Librarymu.calculate_golden_ratio import calculate_golden_ratio  # Sesuaikan dengan path yang benar

def main():
    email_functions = EmailFunctions()

    while True:
        email_functions.display_menu()
        choice = input("Masukkan pilihan: ")

        if choice == '1':
            to_email, subject, message = email_functions.get_email_info()
            email_functions.send_email(subject, message, to_email)
        elif choice == '2':  # Opsi baru untuk menghitung Golden Ratio
            golden_ratio = calculate_golden_ratio()
            print(f"Nilai Golden Ratio adalah: {golden_ratio}")
        elif choice == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
