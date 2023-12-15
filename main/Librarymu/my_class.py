# File: Librarymu/email_functions.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Librarymu.calculate_golden_ratio import calculate_golden_ratio

class EmailFunctions:
    def __init__(self):
        pass

    def send_email(self, subject, message, to_email):
        from_email = "nurridwan270305@gmail.com"  # Ganti dengan email pengirim
        password = "apriliapertiwi27"  # Ganti dengan password email pengirim

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print("Email berhasil dikirim!")
        except Exception as e:
            print("Gagal mengirim email:", str(e))

    def get_email_info(self):
        to_email = input("Masukkan email penerima: ")
        subject = input("Masukkan subjek email: ")
        message = input("Masukkan pesan email: ")
        return to_email, subject, message

    def display_menu(self):
        print("\nPilih aksi:")
        print("1. Kirim Email")
        print("2. Hitung Golden Ratio")
        print("0. Keluar")
