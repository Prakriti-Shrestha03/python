from sqlalchemy import create_engine, Column, Integer, String,Float, DateTime, delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base=declarative_base()

class Tasks(Base):
    __tablename__="Tasks"
    id=Column(Integer,primary_key=True)
    description=Column(String)
    due_date=Column(DateTime,nullable=False)

engine=create_engine('sqlite:///task.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

def add_task(descriptions,date):

    new_task=Tasks(description=descriptions,due_date=datetime.date(int(date[0]),int(date[1]),int(date[2])))
    session.add(new_task)
    session.commit()

def remove_task(descriptions):

    session.query(Tasks).filter(Tasks.description==descriptions).delete()
    session.commit()

def view_task():
    for task in session.query(Tasks):
        print(f"{task.description} is due on {task.due_date}")

add_task("homework",date=[2025,1,31])
add_task("assigment",date=[2025,2,7])
add_task("Club Work",date=[2025,2,4])
view_task()
remove_task("homework")
view_task()