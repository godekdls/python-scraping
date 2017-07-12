import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import time
import getpass

def sendMail(subject, body):
    # https://mail.naver.com/option/imap you should admit of SMTP
    naverId=input("Enter your naver id: ")
    password = getpass.getpass("Enter your Password: ")

    msg = MIMEText(body)
    msg['Subject'] = subject
    emailAddress = naverId + "@naver.com"
    msg['From'] = emailAddress
    msg['To'] = emailAddress

    s = smtplib.SMTP("smtp.naver.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(naverId, password)
    s.send_message(msg)
    s.quit()

context = ssl._create_unverified_context()
html = urlopen("https://isitchristmas.com", context=context)
bsObj = BeautifulSoup(html, "html.parser")
if bsObj.find("a", {"id":"answer"}).attrs['title'] != "YES":
    sendMail("It's not Christmas!", "According to http://itischristmas.com, it is not Christmas!")
    print("email has been sent! check your email")