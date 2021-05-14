# Ciclo While


print()

print('=== Ciclo while ===')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
while i < len(numeros):
    print(f'{i}: {numeros[i]}')
    i += 1

print()

print('=== Suma de los elementos de una lista ===')

i = 0
total = 0
while i < len(numeros):
    total += numeros[i]
    i += 1


print('Lista de numeros: ', numeros)
print('La suma de la lista es: ', total)

print()

print('=== Sumar numeros pares con ciclo while ===')

numeros.append(100)

i = 0
total = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        total += numeros[i]
    i += 1

print('Suma de los numeros pares: ', total)

print()

print('=== Terminacion arbitraria de un ciclo while ===')

total = 0
while True:
    numero = int(input('Escriba un numero entero positivo (Cero para terminar): '))
    if numero == 0:
        break
    
    total += numero

print()
print('Acumulado: ', total)

