# Ejercicio 5.7: Seleccionar de forma aleatoria un elemento de una lista.

import random

print()

numeros = list(range(1, 101))

print(numeros)

print()

print('== Solucion 1 - random.choice() ==')

elegido = random.choice(numeros)

print('Seleccionado el numero: ', elegido)

print()