import requests
from bs4 import BeautifulSoup

url="https://www.bbc.com"

response=requests.get(url)
if response.status_code==200:
    print("Page fetched successfully.")
    soup=BeautifulSoup(response.text,'html.parser')
    #<h2 data-testid="card-headline" class="sc-8ea7699c-3 hlhXXQ">European stock markets fall as Trump says he will hit EU with tariffs<!-- --></h2>
    headlines=soup.find_all("h2",class_="sc-8ea7699c-3")
    print("Top 10 Headlines:")
    for i,headline in enumerate(headlines[:10]):
        print(f"{i+1}.{headline.get_text()}")
else:
    print(f"Failed to retrieve data.Status Code {response.status_code}")