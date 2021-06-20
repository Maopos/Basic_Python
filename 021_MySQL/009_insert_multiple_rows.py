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
val = [('Jennifer Sepulveda', 'Barranquilla Atántico'),
        ('Verónica Posada', 'Sogamoso Boyacá'),
        ('Violeta', 'Dosquebradas Risaralda')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, 'Records inserted.')

print()
print('======================')