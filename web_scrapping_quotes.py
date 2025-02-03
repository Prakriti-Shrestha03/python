import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"
response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

quotes=soup.find_all('span',class_='text')
authors=soup.find_all('small',class_='author')
tags=soup.find_all('div',class_='tags')

for quote,author,tag in zip(quotes,authors,tags):
    print(f"Quote:{quote.text}")
    print(f"Author:{author.text}")
    print("Tag: ")
    for t in tag.find_all('a',class_="tag"):
        print(f"-{t.text}")
    print()