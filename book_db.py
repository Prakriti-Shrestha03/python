import sqlite3

connection=sqlite3.connect("Book.db")
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS BOOK(
               id INT PRIMARY KEY,
               title STRING NOT NULL,
               author STRING NOT NULL,
               price FLOAT NOT NULL)""")

cursor.execute("INSERT INTO BOOK(title,author,price) VALUES (?,?,?)",("Perks of being a wallflower","Stephen Chobosky",500.50))
cursor.execute("INSERT INTO BOOK(title,author,price) VALUES (?,?,?)",("Percy Jackson and the Lightening Theif","Rick Riordan",450.99))
cursor.execute("INSERT INTO BOOK(title,author,price) VALUES (?,?,?)",("A Happy Death ","Albert Camus",800))
connection.commit()

cursor.execute("SELECT * FROM BOOK")
for row in cursor.fetchall():
    print(row)

connection.close()