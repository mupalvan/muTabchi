import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.execute("SELECT id from member")
member = []
for row in cursor:
    member.append(row[0])
print(member)
conn.close()