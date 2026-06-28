from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#URL of the product
url = "https://www.amazon.in/Amkette-Brightness-Laser-Etched-Multi-Media-Connection/dp/B0CPM2QQ5B/ref=sr_1_1?crid=3S7Y76MBK5ZGP&dib=eyJ2IjoiMSJ9.r3d1h94ts-7bLH7zPC-U7B8FdoNk1dbZMNHcRb-yQmqIgzzz6o_5nd374O-i7itwhCKAs5j9gTfNvjpwOihSv5QmI_xTNqQ3osA_FKvLkFtmnBPPMHXhd0GjDWAmS6cQZknaJ03AY8HPJy8lzGFVOrjhzwSgoasqhDU7IIgNA-GHzqF9umdCfzS9zOjDBxH6uaqHX2Z6aYer4UdKVEwzg90DhoUbX96xARKvxmpzuyO7ra0bqMYnzLJbvrppfZ2uIetZZAbOVwlNtyzs4sttjx1xJkwRZQ5W3JpdZXcRjiM.KHGtT42bwNX0d8lMrSCLDTpiyFAkAqMkJDyCdgNB3hs&dib_tag=se&keywords=black%2Bkeyboard%2Bwith%2Bwhite%2Blight&qid=1782668459&s=electronics&sprefix=black%2Bkeyboard%2Bwith%2Bwhite%2Bligh%2Celectronics%2C273&sr=1-1&th=1"

# ====================== Add Headers to the Request ===========================

# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

# A minimal header:

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Adding headers to the request
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")


# Find the HTML element that contains the price
price = soup.find(class_="a-price-whole").get_text()

# Convert to floating point number
price_as_float = float(price)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 800

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )