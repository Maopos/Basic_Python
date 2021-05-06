# Ejercicio 5.8: Calcular la frecuencia (ocurrencias) de los elementos de una lista.

import random
from collections import Counter

print()

paises = ['Argentina', 'Peru', 'Colombia', 'Irak', 'Alemania', 'China', 'Iran', 'Argentina', 'Peru', 'Irak', 'Japon', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Alemania', 'China', 'Iran', 'Argentina', 'Peru', 'Colombia', 'Irak', 'Alemania', 'China', 'Iran', 'Argentina']

se_busca = random.choice(paises)

print('Se busca', se_busca)

print('===========\n')

conteo = paises.count(se_busca)

print('El pais se encontro', conteo, 'veces con .count.')


contador = 0

for i in paises:
    if se_busca == i:
        contador += 1

print('El pais se encontro', contador, 'veces con for.')
print('===========\n')

frecuencia = {}

for n in paises:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1
        
print('Frecuencia de los paises: ', frecuencia)
print('Cantidad de paises: ', len(frecuencia))
print('===========\n')

contador = Counter(paises)
print('Frecuencia de los paises: ', contador)
print('Cantidad de paises: ', len(contador))
print('===========\n')



print()
