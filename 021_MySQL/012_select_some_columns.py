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

mycursor.execute('SELECT name, address FROM customers')

myresult = mycursor.fetchall()

listado = []
for i in myresult:
    listado.append(i)

print(listado)


print()
print('======================')