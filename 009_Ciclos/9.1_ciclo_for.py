# Ciclo For

print()

numeros = [1, 2, 3, 4, 5, 100]

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)



print(numeros)

total = 0
total2 = 0
total3 = 0

for i in numeros:
    total += i

print(f'La suma de los numeros del {numeros[0]} al {numeros[-1]} es: ', total)

for i in range(0, len(numeros)):
    total2 += numeros[i]

print(f'La suma de los numeros del {numeros[0]} al {numeros[-1]} es: ', total2)

print()

print('== Suma de numeros pares ==')

for i in numeros:
    if i % 2 == 0:
        total3 += i

print(f'La suma de los numeros pares del {numeros[0]} al {numeros[-1]} es: ', total3)

print()

print('== Ciclo for mejorado. ==')

total4 = 0

for i in numeros:
    total4 += i

print(f'La suma de los numeros del {numeros[0]} al {numeros[-1]} es: ', total4)


print()

print('== Lista de comprension ==')

total = [numeros[i] for i in range(len(numeros))]

print('Elementos de la lista: ', total)

total = sum([numeros[i] for i in range(len(numeros))])

print('Suma de los elementos de la lista: ', total)

print()

print('== Suma de pares e impares con lista de compresion. ==')

total = sum([i for i in numeros if i % 2 == 0])

print('La suma de los pares: ', total)

print()

print('== Iteracion con for y enumarate ==')

for i, v in enumerate(numeros):
    print(f'{i}: {v}')

print()