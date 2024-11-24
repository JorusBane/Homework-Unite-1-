import sqlite3
from texts import *
from config import *


connection = sqlite3.connect("initiate.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER NOT NULL,
title TEXT NOT NULL,
discription TEXT NOT NULL,
price INTEGER NOT NULL
)
''')

def get_all_products(product_id, title, discription, price):
    check_product = cursor.execute("SELECT * FROM Products WHERE id=?", (product_id, ))


    if check_product.fetchone() is None:
        cursor.execute(f'''
            INSERT INTO Products VALUES("{product_id}","{title}","{discription}",{price} )
        ''')
    connection.commit()

get_all_products(1, "БЦАА", bcaa, bcaa_cost )
get_all_products(2, "Креатин", creatine, creatin_cost)
get_all_products(3, "Протеин", protein, protein_cost)
get_all_products(4, "Аминокислоты", amino_acid, amino_acid_cost)

cursor.execute("UPDATE Products SET discription=? WHERE title =?", (amino_acid, "Аминокислоты"))
cursor.execute("SELECT title, discription, price FROM Products ")
products = cursor.fetchall()


connection.commit()
connection.close()