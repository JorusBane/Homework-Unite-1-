import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# for i in range(10):
#     cursor.execute("INSERT INTO Users (Username, email, age, balance) VALUES (?, ?, ?, ?)",
#                 (f"User{i}", f"example{i}", f"{i}0", f"{i}000"))
#
# for i in range(0,10, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))
#
# for i in range(0, 10, 3):
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}", ))
#
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
# users = cursor.fetchall()
#
# for user in users:
#     print(user)
#
# cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))

cursor.execute("SELECT COUNT(*) FROM Users ")
total_count = cursor.fetchone()[0]
print(f"Количество пользователей: {total_count}")

cursor.execute("SELECT SUM(balance) FROM Users ")
total_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {total_balance}")

cursor.execute("SELECT AVG(balance) FROM Users ")
total_average = cursor.fetchone()[0]
print(f"Средний показатель баланса пользователей: {total_average}")

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
connection.commit()
connection.close()