from sqlalchemy import create_engine,Column, Integer, Float,String, delete, CheckConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Books_Lib(Base):
    __tablename__="Books_Lib"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    author=Column(String)
    genre=Column(String)
    rating=Column(Float)

    __table_args_=(
        CheckConstraint('rating>00 AND rating<=5',name='check_rating')
    )

engine=create_engine("sqlite:///book_lib.db")
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

def add_books(names,authors,genres,ratings):

    new_book=Books_Lib(name=names,author=authors,genre=genres,rating=ratings)
    session.add(new_book)
    session.commit()

def remove_book(name):
    session.query(Books_Lib).filter(Books_Lib.name==name).delete()
    session.commit()
    print("Book Removed.")

def search_book(name):
    x=session.query(Books_Lib).filter(Books_Lib.name==name).first()
    print("Book Found.")
    print(f"Book name:{x.name}\nAuthor={x.author}\nGenre={x.genre}\nRating={x.rating}")

while True:
    print("""You can enter the Library DataBase 
          Your options are 
          1.Add Books
          2.Remove Books
          3.Search Books
          4.Leave
          """)
    
    x=int(input("Enter your choice"))

    if x==1:
        name=input("Enter the books Name")
        author=input("Enter the Author's name")
        genre=input("Enter the genre")
        rating=float(input("Rate it out of 5"))
        add_books(name,author,genre,rating)
    
    if x==2:
        name=input("Enter the book you want to remove")
        remove_book(name)

    if x==3:
        name=input("Enter the book you want to search")
        search_book(name)

    if x==4:
        break
