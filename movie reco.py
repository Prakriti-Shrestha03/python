import requests
from sqlalchemy import create_engine,Column,Integer,Float,String, desc
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

key="725fa1a6772d3d6abe0536325a0a41ca"
url1=f"https://api.themoviedb.org/3/search/movie?query=All&api_key={key}"

url2="https://www.freetestapi.com/api/v1/movies"

Base=declarative_base()

class Movies(Base):
    __tablename__="Movies"
    id=Column(Integer,primary_key=True)
    Title=Column(String)
    Rating=Column(String)
    Genre=Column(String)
    Plot=Column(String)

engine=create_engine("sqlite:///movie.db")
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

response=requests.get(url2)
if response.status_code==200:
    print("Data Fetched.")
    data=response.json()

    for movie in data:
        genre=movie["genre"]
        genres=",".join(genre)
        new_movie=Movies(id=movie["id"],Title=movie["title"],Rating=movie["rating"],Genre=genres,Plot=movie["plot"])
        session.add(new_movie)
    session.commit()
    print("Movie Added.")

else:
    print(f"Error.{response.status_code}")

x=input("Enter the genre you like")
print("The recommended movies are:")
y=session.query(Movies).filter(Movies.Genre.ilike(f"%{x}%")).order_by(Movies.Rating.desc()).all()
with open("recommendation.csv",mode="a",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Title","Rating"])
    for a in y:
        print(f"{a.Title} with rating {a.Rating}")
        writer.writerow([a.Title,a.Rating])
    

