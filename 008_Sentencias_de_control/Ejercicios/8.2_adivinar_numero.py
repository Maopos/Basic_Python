# Ejercicio 8.2. Pedir al usuario que adivine un número. Sólo un intento.

print()

import random

"""
conjunto = list(range(1, 11))
elegido = random.choice(conjunto)
"""

aleatorio = random.randint(1, 10)


print('Adivina un numero entre 1 y 10')
print('==============================\n')

print()


numero = int(input('Escribe un numero entre 1 y 10: '))

if numero == aleatorio:
    print('Correcto!!! :)')
else: 
    print(f'No has adivinado, el numero era {aleatorio}. :(')

print()