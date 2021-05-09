# Ejercicio 8.5. Dadas las rectas y = 2x - 2, y = x + 1, x = 10 comprobar si un punto está en el área comprendida entre las rectas.

print()

# rectas y = 2x - 2, y = x + 1, x = 10

x = float(input('Escriba el valor de X: '))
y = float(input('Escriba el valor de Y: '))



if x <= 10:
    valor_1 = 2 * x - 2
    valor_2 = x + 1

    if valor_2 <= y <= valor_1:
        print(f'El punto ({x}, {y}) SI se encuentra dentro del area asignada.')
    else:
        print(f'El punto ({x}, {y}) NO se encuentra dentro del area asignada.')

else:
    print(f'El punto ({x}, {y}) NO se encuentra dentro del area asignada.')

print()