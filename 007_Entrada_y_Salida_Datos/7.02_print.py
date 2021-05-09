# Salida de datos funcion - print()

print()

nombre = 'Mauricio Posada'
edad = 40
correo = 'maopos@icloud.com'

print('Nombre: ', nombre, end=' *** ')
print('Edad: ' + str(edad))

print()

print('Aprendiendo el uso de la', end=' ')
print('funcion print().')

print('===================\n')

print(nombre, edad, correo, sep=' - ')

print()

colores = ('Amarillo', 'Azul', 'Rojo', 'Verde')
print(colores)

print()

print(colores[0], colores[1], colores[2], colores[3], sep=' == ')

print()

print(*colores, sep=' == ')

print()