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

sql = 'DELETE FROM customers WHERE address = "Pereira Risaralda"'

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Records deleted.")


print()
print('======================')