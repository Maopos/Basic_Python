# Ejercicio 9.6: Encontrar todos los números pares que hay en el rango 100 a 400.

print()

numeros = list(range(100, 401))
pares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)
print('Cantidad de pares: ', len(pares))

print()