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

sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('Toreto', 'Pereira Risaralda')

mycursor.execute(sql, val)

mydb.commit()

print('1 Record inserted, ID: ', mycursor.lastrowid)

print()
print('======================')