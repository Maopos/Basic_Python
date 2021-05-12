# Ejercicio 9.9: Construir un patrón con asteriscos que represente la letra Z.

print()

space = 10

for i in range(8):
    if i == 0 or i == 7:
        for j in range(7):
            print('* ', end='')
    else:
        print(' ' * space + '*', end='')
        space -= 2
    print()

print()