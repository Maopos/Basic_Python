import mysql.connector

print('======================')
print()

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Python2222.',

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE base_datos")

print()
print('======================')