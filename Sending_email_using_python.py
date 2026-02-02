from dotenv import load_dotenv
import os
from Email_access_from_mysql import email_retrival

import smtplib 
from email.message import EmailMessage

load_dotenv()
Email = os.getenv('Email')
Email_App_Password = os.getenv('Email_App_Password')

msg = EmailMessage()
msg['Subject'] = 'This is a demo mail to see automate emails to clients via python'
msg['From'] = Email
msg['To'] = email_retrival()
msg.set_content('How r u')

with smtplib.SMTP('smtp.gmail.com', 587) as server:    
    server.set_debuglevel(1)
    server.starttls()
    server.login(Email,Email_App_Password)
    server.send_message(msg)
    server.quit()
