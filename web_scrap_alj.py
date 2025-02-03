import requests
from bs4 import BeautifulSoup

url="https://www.aljazeera.com/"
response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")
#<h3 class="article-card__title"><span>Trump tariffs live: EU shares tumble after Canada, China, Mexico trade wars</span></h3>
titles=soup.find_all("h3",class_="article-card__title")
i=0
for t in titles:
    print(i+1,t.text)
    i+=1