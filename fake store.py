import requests
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import create_engine,Column,Integer,Float,String,delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

sender_email="Pra0000kri@gmail.com"
password="zjql zjom hmam amzq"

url="https://fakestoreapi.com/products"
response=requests.get(url)

Base=declarative_base()

def create_csv():
    with open("buyer.csv",mode="w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Product","Quantity","Price","Email"])
    print("CSV Created.")

     
class Orders(Base):
    __tablename__="Orders"
    Cust_id=Column(Integer,primary_key=True)
    Products=Column(String)
    Quantity=Column(Integer)
    Price=Column(Float)
    Email=Column(String)

engine=create_engine("sqlite:///order.db")
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

def add_order(id,quantity,email):
    if response.status_code==200:
        print("Data Fetched successfully.")
        global data
        data=response.json()

        for product in data:
            if product["id"]==id:
                new_order=Orders(Products=product["title"],Quantity=quantity,Price=product["price"],Email=email)
                session.add(new_order)
                session.commit()

def delete_order(email):
     session.query(Orders).filter(Orders.Email==email).delete()
     session.commit()

def update_order(new_id,quantity,email):
     x=session.query(Orders).filter(Orders.Email==email).first()
     for products in data:
          if products["id"]==new_id:
               x.Products=products["title"]
               x.Quantity=quantity
               x.Price=products["price"]
     session.commit()

def add_in_csv():
     with open("buyer.csv",mode="a",newline="")as file:
          writer=csv.writer(file)
          for Product in session.query(Orders):
               writer.writerow([Orders.Products,Orders.Quantity,Orders.Price,Orders.Email])

               
