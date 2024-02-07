import smtplib, ssl

smtp_server = "smtp.gmail.com"
smtp_port = 587  # For starttls

sender_email = "psousa@twilio.com"  # Enter your address
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.connect(smtp_server, smtp_port)
    server.login(sender_email, password)
    # server.sendmail('{from_email}', '{to_email}', '{message}')
    print('It worked!')
# catch exceptions in case connection may not be upgraded to secure    
except Exception as e:
    print(f'Error: {e}')
finally:    
    server.quit() # Close the connection 
    print('Connection closed')
