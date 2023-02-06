from keys_config import *

import smtplib
from email.mime.multipart import MIMEMultipart # standard python library
from email.mime.text import MIMEText
from twilio.rest import Client

twilio_client = Client(Twilio_account_SID, Twilio_token)#  Send the message

def inform(message_to_send):
    try:
        message = twilio_client.messages.create(
                                body=message_to_send,
                                from_=Twilio_phone,
                                to=Reciep_Phone
                            )
        print(message_to_send)
    except:
        print('problem with Twillio')

def send_email(mail_subject, df_test):
    msg = MIMEMultipart() #Setup the MIME
    msg['From'] = 'Lemon Paper'
    msg['To'] = receiver_address
    msg['Subject'] = mail_subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #enable security
    server.login(sender_address, sender_pass) # login with mail_id and password

    html = """\
    <html>
    <head></head>
    <body>
        {0}
    </body>
    </html>
    """.format(df_test.to_html())
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    server.sendmail(sender_address, receiver_address, msg.as_string())
    server.quit()
