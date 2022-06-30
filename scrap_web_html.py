import requests
import re
from bs4 import BeautifulSoup

gpu = input("What product you want to search for? ")
# url = f"https://www.neweg.ca/p/pl?d={gpu}"
url = "https://www.newegg.ca/p/pl?d=3080"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
print(page_text)



