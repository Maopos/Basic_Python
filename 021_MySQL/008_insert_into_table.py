import mysql.connector

print('======================')
print()

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password ='Python2222.',
    database = 'base_datos'

)

mycursor =mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mauricio Posada", "Ibague Tolima")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'Records inserted.')



print()
print('======================')