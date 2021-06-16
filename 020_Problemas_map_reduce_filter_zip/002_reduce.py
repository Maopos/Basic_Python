''' Problema #2:
Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función reduce. '''

from functools import reduce

print('======================')
print()

listado = [1, 2, 3, 4]


numero = reduce(lambda x, y: x * 10 + y, listado)

print(numero)

print()
print('======================')