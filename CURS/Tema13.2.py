import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurații email
SMTP_SERVER = "smtp.example.com"  # Înlocuiește cu serverul SMTP corespunzător
SMTP_PORT = 587
EMAIL_SENDER = "expeditor@example.com"
EMAIL_PASSWORD = "parola_securizată"
EMAIL_RECEIVER = "destinatar@example.com"

# Folder de monitorizat
FOLDER_TO_WATCH = "Rapoarte/"


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        filename = event.src_path
        if filename.endswith(".txt"):
            print(f"Fișier detectat: {filename}")
            send_email_notification(filename)


def send_email_notification(filename):
    """Trimite un email de notificare despre fișierul nou."""
    subject = "A fost încărcat un nou raport"
    body = f"Un nou fișier raport a fost adăugat în folder: {filename}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp.mail.yahoo.com, 465) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("Email trimis cu succes!")
    except Exception as e:
        print(f"Eroare la trimiterea emailului: {e}")


def start_monitoring():
    """Pornește monitorizarea folderului."""
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"Monitorizare începută în folderul: {FOLDER_TO_WATCH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_monitoring()
