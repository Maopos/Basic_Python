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

sql = 'SELECT * FROM customers ORDER BY name'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)


print()
print('======================')