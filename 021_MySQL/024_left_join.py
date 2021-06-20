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

sql = "SELECT \
  customers.name AS customer, \
  foods.comidas AS food \
  FROM customers \
  LEFT JOIN foods ON customers.favorites = foods.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)


print()
print('======================')