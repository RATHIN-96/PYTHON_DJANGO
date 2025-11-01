import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rathin@123",
    database="Newstud"
    
)

print(mydb)
 
mycursor=mydb.cursor()
# mycursor.execute("create database Newstud")
# mycursor.execute("CREATE TABLE customer(name VARCHAR(40),place VARCHAR(50))")

# sql='INSERT INTO customer(name,place)VALUES("Ram","Kozhikode")'
# mycursor.execute(sql)
# mydb.commit()
# print('data inserted')

# sql='INSERT INTO customer(name,place)VALUES(%s,%s)'
# VAL =[('Rohan','Kannur'),('Anu','Wayanad'),('Abhishek','Malapuram')]
# mycursor.executemany(sql,VAL)
# mydb.commit()
# print('data inserted')

# mycursor.execute('select * from customer')
# x = mycursor.fetchall()
# y = mycursor.fetchone()
# d = mycursor.fetchmany()
# print(x)
# print(y)
# print(d)



# for i in x:
#     print(i)
# for i in y:
#     print(i)
# for i in d:
#     print(i)

# sql = 'update customer set name = "Rathin" where place= "Kozhikode"'
# mycursor.execute(sql)
# mydb.commit()
# mydb.close()
# print('Success full')

# mycursor.execute('drop table customer')
# mycursor.execute('drop database Newstud')
