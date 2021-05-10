# Ejercicio 9.7: Construir un patrón con asteriscos que represente la letra E.

print()

for i in range(7):
    if i == 0 or i == 6:
        print('*' * 5, end='')
    elif i == 3:
        print('*' * 4, end='')
    elif i != 0 and i != 3 and i != 6:
        print('*', end='')

    print()

print()