from bs4 import BeautifulSoup
import requests
import smtplib
from config import MY_EMAIL, MY_PASSWORD
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US",
}

my_email = MY_EMAIL
password = MY_PASSWORD

#https://www.amazon.in/Jujutsu-Kaisen-SatoruUnisex-Hoodie-Lilac/dp/B0BR98RVDB/ref=cs_sr_dp_2?crid=2CUTWIKVBOE1Y&keywords=hoodies%2Bfor%2Bmen&qid=1698134422&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=hoodie%2Caps%2C238&sr=8-9&th=1&psc=1
url = input("Please give us the url of the product you want to buy : ")
response = requests.get(url, headers=headers)
amazon_product = response.text
soup = BeautifulSoup(amazon_product, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
float_price_without_currency = float(price.split("₹")[1])
your_price = float(input("Please give us your desired price for the product :"))
your_email = input("Please give us your email : ")

title = soup.find(id="productTitle").get_text().strip()

if float_price_without_currency <= your_price:
    message = f"{title} is now {price}\nThank you!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=your_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
                            )