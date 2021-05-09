# Ejercicio 8.4. Dada la recta y = 6x + 10, comprobar si un punto dado pertenece a ella.

print()

# recta y = 6x + 10

x = float(input('Escriba el valor de X: '))
y = float(input('Escriba el valor de Y: '))

valor = 6 * x + 10

if valor == y:
    print(f'El punto ({x}, {y}) SI pertenece a la recta y = 6x + 10.')
else:
    print(f'El punto ({x}, {y})  NO pertenece a la recta y = 6x + 10.')
    

print()