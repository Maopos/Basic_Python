import mysql.connector

   
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Python2222.'
)

print(mydb)