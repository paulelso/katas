import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 465  # For SSL

sender_email = "psousa@twilio.com"  # Enter your address
sender_name = "Paulo Sousa (Twilio)"
password = input("Type your password and press enter: ")

receiver_email = "paulelso@gmail.com"
subject = "Multipart test email from Python"
message = MIMEMultipart("alternative")
message["From"] = sender_name
message["To"] = receiver_email
message["Subject"] = subject

# Plain-text message version
text = """\
Hi,

This a a plain text email from Python.
"""

# HTML message version
html = """\
<!DOCTYPE html>
<html>
    <body>
        <p>Hi,</p>
        <p>This is an HTML email from Python.</p>
    </body>
"""

# Convert the plain-text and HTML message into MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Create an unverified context
context = ssl._create_unverified_context()

# Create a secure SSL context. This gave a ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
# context = ssl.create_default_context()

# Thinking of connecting to the smtp server like opening a file.
# Initiate connection, do something with the connection, close the connection.
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password) # Log in to the server
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    ) # Send the email
    print('Email sent successfully') # Confirm email was sent