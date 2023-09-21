import smtplib
import ssl
from email.message import EmailMessage

# Declaring own variables and inputs
subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = ""
receiver_email = ""
password = input("Enter password for " + sender_email + ": \n")

# Build the message frame
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

# Send the mail
context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)

print("Sending email!")
print(ssl.OPENSSL_VERSION)
with smtplib.SMTP("smtp-mail.outlook.com", 587, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent succesfully!")