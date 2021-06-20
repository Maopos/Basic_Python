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


sql = "UPDATE customers SET id = '5' WHERE id = '10'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


print()
print('======================')