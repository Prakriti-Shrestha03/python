import requests
from bs4 import BeautifulSoup

url="https://www.w3schools.com/python/default.asp"
response=requests.get(url)

#<a href="/html/default.asp" class="ga-nav subtopnav_firstitem" title="HTML Tutorial">HTML</a>

soup=BeautifulSoup(response.text,"html.parser")

a_tag=soup.find_all("a",href=True)
print("All items A tag contains")
for i in a_tag:
    print(i["href"])

