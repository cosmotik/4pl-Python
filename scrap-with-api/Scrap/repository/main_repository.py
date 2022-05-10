import requests
from bs4 import BeautifulSoup


def root():
    URL = "https://pigu.lt/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="product-price")
    return {"message": results.text}
