# SMTP is a => Simple Mail Transfer Protocol
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Shubham'
email['to'] = 'shubamkharche2144@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'


email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shubham@gmail.com', 'shubham@123')
    smtp.send_message(email)
    print('All good boss!')
# This code will send email to the given email address.
# The email will be sent from the given email address.u