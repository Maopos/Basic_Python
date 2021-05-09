# Ciclo For

print()

numeros = [1, 2, 3, 4, 5]

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)
numeros.append(11)
numeros.append(12)
numeros.append(13)
numeros.append(14)
numeros.append(15)


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

print('== Suma de numeros pares ==\n')

for i in numeros:
    if i % 2 == 0:
        total3 += i

print(f'La suma de los numeros pares del {numeros[0]} al {numeros[-1]} es: ', total3)

print()