import sqlite3
from texts import *
from config import *


connection = sqlite3.connect("initiate.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


def add_user(username, email, age):
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username, ))
    if check_user.fetchone() is None:
        cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES( ?, ?, ?, ?)", 
                       (f"{username}", f"{email}", f"{age}", 1000))
    connection.commit()

def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        return False
    return True
