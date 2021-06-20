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

mycursor.execute('SELECT * FROM customers WHERE address like "%ris%"')

myresult = mycursor.fetchall()

for i in myresult:
    print(i)


print()
print('======================')