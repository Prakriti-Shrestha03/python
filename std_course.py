from sqlalchemy import create__engine,Column,Integer,String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Std_Course(Base):
    __tablename__="Std_Course"
    std_id=Column(Integer,primary_key=True)
    name=Column(String)
    course=Column(String)

    
