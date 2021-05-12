# Ejercicio 9.10: Realizar cálculos de estadísticos básicos: media, mínimo, máximo.

import math, random

print()

numeros = []

for i in range(10):
    num = random.randint(100, 1000)
    numeros.append(num)

print(numeros)
print()

suma = 0
minimo = numeros[0]
maximo = numeros[0]

for i in numeros:
    suma += i
    if minimo > i:
        minimo = i
    if maximo < i:
        maximo = i

print('Suma: ', suma)
print('Promedio: ', suma/len(numeros))
print('Minimo: ', minimo)
print('Maximo: ', maximo)


print()