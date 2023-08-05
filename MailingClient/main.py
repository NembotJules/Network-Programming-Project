# import smtplib 
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP('smtp.gmail.com', 587)

# server.starttls()

# #Log to the account...

# server.login('juniorbertrand761@gmail.com', 'ACER2002')

# msg = MIMEMultipart()
# msg['From'] = 'juniorbertrand761@gmail.com'
# msg['To'] = 'juniorbertrand761@gmail.com'
# msg['Subject'] = 'Nothing special just a test'

# with open('message.txt','r') as f: 
#     message = f.read()

# msg.attach(MIMEText(message, 'plain'))

# filename = 'spam.png'
# attachment = open(filename, 'rb')

# p = MIMEBase('application', "octet-stream")
# p.set_payload(attachment.read())

# encoders.encode_base64(p)
# p.add_header("Content-Disposition", f"attachment; filename={filename}")
# msg.attach(p)

# text = msg.as_string()
# server.sendmail('juniorbertrand761@gmail.com', 'juniorbertrand761@gmail.com', text)

# server.quit()
#-----------------------------------------------------

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders

# Email configuration
sender_email = 'email@gmail.com'
sender_appassword = 'fqbwvccztgryzkem'
recipient_email = 'email@gmail.com'
subject = 'Test Email'
body = 'Mailing Client'

# Create the email content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Create a connection to Gmail's SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.ehlo()
# Log in to the Gmail account
try:
    server.login(sender_email, sender_appassword)
except smtplib.SMTPAuthenticationError as e:
    print("Login failed:", e)
    server.quit()
    exit(1)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())
with open('message.txt','r') as f: 
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'spam.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail('email@gmail.com', 'email@gmail.com', text)

server.quit()
# Close the connection

print('Email sent successfully!')
