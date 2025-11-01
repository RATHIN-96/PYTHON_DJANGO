import sqlite3
mydb =sqlite3.connect('newdb.db')
print(mydb,)

mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE employee (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
# mydb.commit()

sql='INSERT INTO employee (name)values("Vishnu")'
mycursor.execute(sql)
mydb.commit()
print('success',)

