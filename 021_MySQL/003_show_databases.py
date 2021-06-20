import mysql.connector

print('======================')
print()

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Python2222.'
)

mycursor = mydb.cursor()

mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)

print()
print('======================')