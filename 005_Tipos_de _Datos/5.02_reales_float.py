# Numeros de punto flotante - Reales

print()

pi = 3.1415
precio = 29.95

# especificamos cuantos decimales se van a mostrar en el manejador
print('El valor de pi es: %.4f' % pi)
print('El valor de precio es: %.2f' % precio)

print()

print(pi)
print(precio)

print()

print('El tipo de dato de pi es: ', type(pi))
print('El tipo de dato de precio es: ', type(precio))

print()

print('== Operaciones arimeticas con numeros reales - float ==')

pi = pi * 2
print('El nuevo valor de pi es: ', pi)

total = precio * 5

print('El total de la compra es: %.2f' % total)

print()

print('== Creacion de un float desde un string ==')

costo = float(input('Escribe el costo del producto: '))
print('El costo del producto es: %.2f' % costo)
print('El tipo de la variable costo es: ', type(costo))

print()