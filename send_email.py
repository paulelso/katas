import smtplib, ssl

smtp_server = "smtp.gmail.com"
#port = 587  # For starttls
port = 465  # For SSL

sender_email = "psousa@twilio.com"  # Enter your address
password = input("Type your password and press enter: ")

import ssl

# Create an unverified context
context = ssl._create_unverified_context()

# Create a secure SSL context. This gave a ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
# context = ssl.create_default_context()

# Thinking of connecting to the smtp server like opening a file.
# Initiate connection, do something with the connection, close the connection.
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password) # Log in to the server
    print("Connected to the server")