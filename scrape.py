import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = 'https://www.amazon.de/Apple-Retina-Display-prozessor-generation/dp/B07PX85BT3/ref=sr_1_1?crid=OP3M4TEZ7T2B&keywords=imac+27+2019&qid=1568228287&s=gateway&sprefix=imac%2Caps%2C184&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
password = os.environ['gmail_app_password']

def scrape_price(priceToCompare):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    formatted_price = float(price[0:5])
    print(formatted_price)

    if (formatted_price < priceToCompare):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('oldmols@gmail.com', password)

    subject = 'Price fell down!'
    body = f"Check the Amazon link: {URL}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'oldmols@gmail.com',
        'mikemols@me.com',
        msg
    )

    print('Email has been sent!')

    server.quit()

scrape_price(1.700)