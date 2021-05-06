# Ejercicio 5.11: Encontrar los tres valores mayores en un diccionario.

from heapq import nlargest

print()

edades = {'Mauricio': 40, 'Stella': 64, 'Jennifer': 34, 'Sarita': 12, 'Violeta': 8, 'Daniel': 35, 'Libardo': 37}

print('Edades: ', edades)
print('========================================\n')

personas_mayores = nlargest(3, edades, key=edades.get)
print('Las 3 personas mayores son: ', personas_mayores)
print('========================================\n')

print()
