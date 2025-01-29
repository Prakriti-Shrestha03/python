import csv
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email="Pra0000kri@gmail.com"
password="zjql zjom hmam amzq"
csv_file="Task_Reminder.csv"

def create_csv():
    header=["Task","Due Date","Email"]
    with open(csv_file,mode="w") as file:
        writer=csv.writer(file)
        writer.writerow(header)
    print("CSV file created.")


def add_task(task,duedate,email):
    with open(csv_file,mode="a")as file:
        writer=csv.writer(file)
        writer.writerow([task,duedate,email])
    print("Task Added")

def send_remainder():
    task=[]
    email=[]
    with open(csv_file,mode="r")as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(type(row["Due Date"]))
            # if row["Due Date"].month==1:
            #     task.append(row["Task"])
            #     email.append(row["Email"])

    print(task,email)


create_csv()
while True:
    task=input("Enter your task")
    x=input("Enter the dude dat in (Y/M/D) format")
    x=x.split("/")
    duedate=datetime.date(int(x[0]),int(x[1]),int(x[2]))
    email=input("Enter the remainder email address")

    add_task(task,duedate,email)
    y=input("Do you want to add more tasks (yes/no)")
    if y.lower()=="no":
        break
send_remainder()



