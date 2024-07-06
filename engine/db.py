import csv
import sqlite3

conn = sqlite3.connect("jan.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), PATH VARCHAR(1000))"
cursor.execute(query)

# query = r"INSERT INTO sys_command VALUES(null,'one note', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = r"INSERT INTO web_command VALUES(null,'geeksforgeeks', 'https://www.geeksforgeeks.org//')"
# cursor.execute(query)
# conn.commit()


# # Testing Module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name))
# results = cursor.fetchall()
# print(results)

#create table with desired column
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# # Specify the column indices you want to import (0-based index)
# desired_column_indices = [0, 33]
# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_column_indices]
#         cursor.execute('''INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
# conn.commit()
# conn.close()

# # Insert Single contacts (Optional)
# query = "INSERT INTO contacts VALUES (null,'Lakhan', '6394343032', 'null')"
# cursor.execute(query)
# conn.commit()

# Search Contacts from database
query = 'Diksha Tripathi'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])
