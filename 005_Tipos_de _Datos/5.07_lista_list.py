# Tipo de dato - Lista - list

print()

print('== Creacion de una lista ==')

numeros = [2, 4, 6, 8, 10]

print('Tipo de datos: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Acceso a los elementos de una lista. ==')

dos = numeros[0]
print('El primer elemento es: ', dos)
seis = numeros[2]
print('El elemento 3 es: ', seis)
ultimo = numeros[-1]
print('El ultimo elemento es: ', ultimo)

print()

subseccion = numeros[1:4]
print('Tipo de datos: ', type(subseccion))
print('Cantidad de elementos: ', len(subseccion))
print('Contenido', subseccion)

print()

print('== Acceso con desempaquetamiento ==')

cuatro, seis, ocho = subseccion
print(cuatro)
print(seis)
print(ocho)

print()

print('== Modificacion de una lista. ==')

print('Contenido', numeros)
numeros[0] = 1
print('Tipo de datos: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()