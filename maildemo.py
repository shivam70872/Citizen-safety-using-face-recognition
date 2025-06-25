import smtplib
from email.message import EmailMessage

def sendEmail(to, message, subject):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = 'shivam8289021803@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('shivam8289021803@gmail.com', 'flsptehukhzuqxcv')

    server.send_message(msg)
    print('Mail Sent')
    server.quit()

# sendEmail("pragatiarora2706@gmail.com", "Demo Subject", "This is Testing Email")