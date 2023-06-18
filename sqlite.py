import sqlite3

conn = sqlite3.connect('users.db')
conn.execute('''CREATE TABLE member
         (
         id            INT
         );''')
print("Table created successfully")

conn.close()