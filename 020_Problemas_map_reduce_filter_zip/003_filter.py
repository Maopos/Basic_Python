''' Problema #3:
Crear una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Utilizar la función filter. '''


print('======================')
print()

listado = ['Manzana', 'Pera', 'Uva', 'Mango', 'Papaya', 'Piña']

resultado = list(filter(lambda x: x[0] == 'P', listado))

print(resultado)

print()
print('======================')