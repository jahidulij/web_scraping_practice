import requests
import re
from bs4 import BeautifulSoup

search_term = input("What product you want to search for? ")
url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
# url = "https://www.newegg.ca/p/pl?d=3080"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
# pages = str(page_text).split("/")
# pages = str(page_text).split("/")[-2]
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

item_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(text=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string

        item_found[item] = {"Price": int(price.replace(",", "")), "Link": link}

print(item_found)



