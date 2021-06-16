print('======================')
print()

def generarPares(cantidad= 1):
    pares = []
    contador = 1

    while contador <= cantidad:
        if contador % 2 == 0:
            pares.append(contador)
        contador += 1

    if cantidad > 0:
        print(f'\nLos pares entre 0 y {cantidad} son: ', pares, f'\nTotal pares {len(pares)}')

    else:
        print(f'\nEl número debe ser positivo.')

generarPares(int(input('Escriba el rango: ')))

print()
print('======================')