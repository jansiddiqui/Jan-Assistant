import sqlite3

conn = sqlite3.connect("jan.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), PATH VARCHAR(1000))"
cursor.execute(query)

# query = r"INSERT INTO sys_command VALUES(null,'one note', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = r"INSERT INTO web_command VALUES(null,'gmail', 'https://mail.google.com/mail/u/0/#inbox')"
cursor.execute(query)
conn.commit()