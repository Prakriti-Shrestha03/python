import requests
from bs4 import BeautifulSoup

url="https://kissflow.com/application-development/rad/rad-vs-jad-difference/#:~:text=RAD%20lessens%20the%20impact%20of,on%20planning%20and%20sequential%20design.."
response=requests.get(url)
#<table style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; border: 1px solid #99acc2;">

soup=BeautifulSoup(response.text,"html.parser")
data_t=soup.find_all("table")[0]
data_p=data_t.find_all("p")
print("All text in a table are:")
for i in data_p:
    print(i.text)