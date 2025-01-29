import sqlite3

connection=sqlite3.connect("store.db")
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               price REAL NOT NULL)""")

cursor.execute("INSERT INTO products (name,price) VALUES (?,?)",("Laptop",999.99))
connection.commit()

cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

connection.close()