import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Apple-Retina-Display-prozessor-generation/dp/B07PX85BT3/ref=sr_1_1?crid=OP3M4TEZ7T2B&keywords=imac+27+2019&qid=1568228287&s=gateway&sprefix=imac%2Caps%2C184&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    print(converted_price)

    if (converted_price < 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('oldmols@gmail.com', 'zfruedmpazkwfrdw')

    subject = 'Price fell down!'
    body = f"Check the Amazon link: {URL}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'oldmols@gmail.com',
        'mikemols@me.com',
        msg
    )

    print('Email has been sent!')

    server.quit(

check_price()