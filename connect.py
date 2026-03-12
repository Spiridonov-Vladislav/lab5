import sqlite3

connection = sqlite3.connect('myDatabase.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER                                          
)            
''')

cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
users = cursor.fetchall()

for user in users:
    print(user)
connection.commit()
connection.close()

#8659583696:AAFpyHtFKxC_CV7XHKOZHQp9bhq5yfI0ieU

