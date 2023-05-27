import smtplib
import ssl
import os
# first turn on the two step verification on gmail. Then, search for the App password and from the dropdown box
# find the custom, rename it and generate the password and copy and paste it here.


def send_email(message):
    host = 'smtp.gmail.com'
    port = 456  # always for gmail

    username = 'naghmehn85@gmail.com'
    password = os.getenv('PASSWORD')

    context = ssl.create_default_context
    reciever = 'naghmehn85@gmail.com'

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
