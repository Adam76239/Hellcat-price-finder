import requests
from bs4 import BeautifulSoup

url = "https://www.caranddriver.com/dodge/charger-srt-hellcat"

get_url = requests.get(url)
soup = BeautifulSoup(get_url.text,"html.parser")

def extract_price(soup_obj, tag, attribute_name, attribute_value):
    price = soup_obj.find(tag, {attribute_name: attribute_value}).text
    return price

price_point = extract_price(soup, "div", "class","msrp-value")

print("The price of a 2022 Dodge Charger SRT Hellcat is:", price_point)
