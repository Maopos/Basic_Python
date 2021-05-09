# Ejercicio 8.3. Comprobar el producto de mayor precio entre tres productos.

print()

precio_1 = float(input('Escriba el precio del Producto No. 1: '))
precio_2 = float(input('Escriba el precio del Producto No. 2: '))
precio_3 = float(input('Escriba el precio del Producto No. 3: '))

print('===================================\n')

if precio_1 > precio_2 and precio_1 > precio_3:
    print(f'El producto mas costoso es el del Precio de ${precio_1} pesos.')
elif precio_2 > precio_1 and precio_2 > precio_3:
    print(f'El producto mas costoso es el del Precio de ${precio_2} pesos.')
elif precio_3 > precio_1 and precio_3 > precio_2:
    print(f'El producto mas costoso es el del Precio de ${precio_3} pesos.')
elif precio_1 == precio_2 or precio_1 == precio_3:
    pass

print()