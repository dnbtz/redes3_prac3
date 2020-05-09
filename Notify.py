import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time


def send_alert_attached(subject, nom):
    time.sleep(85)
    COMMASPACE = ', '
    mailsender = "dummycuentaredes3@gmail.com"
    mailreceip = "tanibet.escom@gmail.com"
    mailserver = 'smtp.gmail.com: 587'
    password = 'Secreto123@'

    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open('deteccion'+nom+'.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()