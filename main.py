import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(addressee, subject):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remitter = os.environ.get('EMAIL_REMITTER')  # Get sender's email address from environment variable
    password = os.environ.get('EMAIL_PASSWORD')  # Get sender's email password from environment variable

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = remitter  # Sender's email address
    msg['To'] = addressee  # Recipient's email address
    msg['Subject'] = subject  # Email subject

    # Attach HTML content
    with open('index.html', 'r') as file:
        html = file.read()
    msg.attach(MIMEText(html, 'html')) # You can also send a plain text message, msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server and send the email
    with smtplib.SMTP(host=smtp_server, port=smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(remitter, password)  # Login to the sender's email account
        server.send_message(msg)  # Send the email

    print("Email sent!")

if __name__ == "__main__":
    # Get recipient's email address and email subject from user input
    addressee = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email:")

    # Call the send_email function with recipient's email address and subject
    send_email(addressee, subject)