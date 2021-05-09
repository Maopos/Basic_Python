# Ejercicio 8.6. Aplicar descuento según la cantidad de productos comprados. Cada producto cuesta $100.000.

print()

producto = 100000

cantidad = int(input('Digite la cantidad de productos: '))

x = 5
y = 20
z = 50
a = 100

porcentaje_x = 0
porcentaje_y = 1
porcentaje_z = 3
porcentaje_a = 7
porcentaje_b = 10


if cantidad <= 0:
    print('La cantidad debe ser mayor a 0.')
elif cantidad <= x:
    total =  cantidad * producto
elif cantidad <= y:
    total =  cantidad * producto - (cantidad * ((producto  * porcentaje_y) / 100))
elif cantidad <= z:
    total =  cantidad * producto - (cantidad * ((producto  * porcentaje_z) / 100))
elif cantidad <= a:
    total =  cantidad * producto - (cantidad * ((producto  * porcentaje_a) / 100))
else:
    total =  cantidad * producto - (cantidad * ((producto  * porcentaje_b) / 100))
    

print(f'El precio Total de la compra es: {total}')


print()