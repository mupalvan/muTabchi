import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.execute("SELECT id from member")
member = []
for row in cursor:
    member.append(row[0])
    
new_list = [item.strip() for item in member]
print(new_list)
conn.close()