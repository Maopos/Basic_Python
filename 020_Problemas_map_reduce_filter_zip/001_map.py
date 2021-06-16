''' Problema #1:
Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena de texto y retornará una lista. '''

print('======================')
print()

frase = 'Bienvenidos a Python utilizando map'

cantidad_letras = list(map(lambda x: len(x), frase.split()))
cantidad_letras_2 = list(map(len, frase.split()))

print(cantidad_letras)
print(cantidad_letras_2)


print()
print('======================')