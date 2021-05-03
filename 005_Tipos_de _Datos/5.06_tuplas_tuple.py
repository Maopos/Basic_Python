# Tipo de dato compuesto - Tupla - estatico

print()

punto = (2, 5)
print('Tipo de dato', type(punto))
print(punto)
print('Cantidad de  elementos:', len(punto))

print()

# Acceso a los elementos de una Tupla

x = punto[0]
y = punto[1]

print('El valor de x es: ', x)
print('El valor de y es: ', y)

print()

# Desempaquetamiento:

abscisa, ordenada = punto
print('El valor de x es: ', abscisa)
print('El valor de y es: ', ordenada)

print()

# Acceso con indice negativo

ultimo_elemento = punto[-1]
penultimo_elemento = punto[-2]
print('El valor de x es: ', penultimo_elemento)
print('El valor de y es: ', ultimo_elemento)

print()

# Inmutabilidad

# punto[0] = 3 // Genera Type error

punto = (3, 7) # Se puede reemplazar el contenido de la varible
print(punto)

print()

# Iteracion de una tupla

primos = (2, 3, 5, 7, 11, 13, 17, 19)

print('Cantidad de elementos: ', len(primos))

print()

print('== Iteracion con while ==')

i = 0
while i < len(primos):
    print(f'El elemento en el indice {i} es igual a {primos[i]}')
    i += 1

print()

print('== iteracion con ciclo for ==')

for i in range(len(primos)):
    print(f'El elemento en el indice {i} es igual a {primos[i]}')
    
    
print()

print('== Iteracion de una tupla con enumerate ==')
print(primos)
for i, v in enumerate(primos):
    print(f'{i}: {primos[i]}')

print()

# Mecanismos alternativos para crear tuplas
# Modo A:

numeros = 1, 2, 3
print('Tipo de datos de la variable numeros: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
for i, v in enumerate(numeros):
    print(f'{i}: {numeros[i]}')

print()

numeros = 1,
print('Tipo de datos de la variable numeros: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
for i, v in enumerate(numeros):
    print(f'{i}: {numeros[i]}')


print()

# Modo B:

numeros = tuple([9])
print('Tipo de datos de la variable numeros: ', type(numeros))
print('Cantidad de elementos: ', len(numeros))
for i, v in enumerate(numeros):
    print(f'{i}: {numeros[i]}')

print()

print('== Operaciones clase tuple ==')

colores = 'negro', 'blanco', 'negro', 'azul', 'negro', 'rojo', 'azul', 'verde'
print(colores.count('negro')) 
print(colores.index('rojo'))
print()