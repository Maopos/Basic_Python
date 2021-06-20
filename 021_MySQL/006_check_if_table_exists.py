import mysql.connector

print('======================')
print()

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Python2222.',
    database = 'base_datos'
)

mycursor = mydb.cursor()

mycursor.execute('SHOW TABLES')

for i in mycursor:
    print(i)
    print(type(i))

print()
print('======================')