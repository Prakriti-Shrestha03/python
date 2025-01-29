from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class User(Base):
    __tablename__='User'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)

engine=create_engine('sqlite:///user.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

new_user=User(name="John Doe",email="johnd@gmail.com")
session.add(new_user)
session.commit()

session.query(User).filter(User.name=="John Doe").update(User.email=="jane.doe@example.com")
session.commit()
