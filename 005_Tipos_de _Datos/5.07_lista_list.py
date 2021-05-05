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

print('== Acceso a un indice no existente ==')
# valor = numeros[-6]
# print(valor)

print()

print('== Modificacion de una lista. ==')

print('Contenido', numeros)
numeros[0] = 1
print('Tipo de datos: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Modificar lista con numeros negativos ==')

numeros[-1] = 12
print('Tipo de datos: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Ciclo While ==')

i = 0
while i < len(numeros):
    print(f'{i}: {numeros[i]}')
    i+= 1

print()
print('== Modo inverso ==')

i = len(numeros)-1
while i >= 0:
    print(f'{i}: {numeros[i]}')
    i-= 1


print()

print('== Iteracion con ciclo for ==')

for i in range(0, len(numeros)):
    print(f'{i}: {numeros[i]}')

print()

print('== Modo inverso ==')
for i in range(len(numeros)-1 , -1, -1):
    print(f'{i}: {numeros[i]}')

print()

print('== Iteracion por elemento ciclo for ==')

for n in numeros:
    print(n)

print()

print('== Iterar lista con enumerate ==')

for i, n in enumerate(numeros):
    print(f'{i}: {n}')

print()

print('== Operaciones listas ==')
print()

print('== Insertar - append() - al final ==')
numeros.append(14)
print('Tipo de datos: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Insertar - insert() - en un lugar definido ==')
numeros.insert(1, 2)
numeros.insert(8, 2)
numeros.insert(4, 2)
numeros.insert(6, 2)
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Remover elementos - remove() - el elemento indicado ==')
numeros.remove(1)
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)

print()

print('== Remover elementos - pop() - el elemento de la posicion indicada ==')
borrado = numeros.pop(4)
print('Cantidad de elementos: ', len(numeros))
print('Contenido', numeros)
print(f'Se ha borrado el numero: {borrado}')

print()

print('== Contar elementos - count()  ==')
buscar = 2
contador = numeros.count(buscar)
print('Lista: ', numeros)
print(f'Se encontraron {contador} coincidencias del numero: {buscar}')

print()

print('== Invertir el orden de la lista - reverse() ==')

numeros.reverse()
print(numeros)

print()

print('== Remover elementos de la lista - clear() ==')

numeros.clear()
print(numeros)

print()