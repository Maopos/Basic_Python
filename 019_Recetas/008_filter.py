print('======================')
print()

print('=== Filtrar ints y tulas de una lista ===')

numeros = [2001, (1, 2, 3, 4, 5), (6, 7, 8, 9, 0)]

resultado_1 = list(filter(lambda x: type(x) == int, numeros))
resultado_2 = list(filter(lambda x: type(x) == tuple, numeros))

print(resultado_1)
print(resultado_2)

print('\n=== Numeros pares ===')

listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

resultado_3 = list(filter(lambda x: x % 2 == 0 and x != 0, listado))

print(resultado_3)

print()
print('======================')