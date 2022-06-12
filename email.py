
import smtplib
'''SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon'''
import ssl
# Secure Sockets Layer // Encryptian for both client and server peer authentication
from email.message import EmailMessage # Email

subject = "Email"
body = "test"
sender_email = "joeyschnepel@gmail.com"
receiver_email = "joeyschnepel@gmail.com"
password = input("Password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Using HTML to add a little bit of a format

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sent")


# Email Authorization and server connection
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")