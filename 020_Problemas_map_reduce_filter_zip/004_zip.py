''' Problema #4:
Realizar una función que tome una lista de comprensión para devolver una lista de la misma longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre ellas. Ejemplo: Listas: ['A', 'a'] ['B','b'] Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función zip. '''

print('======================')
print()

lista_1 = ['A', 'B', 'C', 'D', 'E']
lista_2 = [10, 20, 30, 40, 50]

resultado = list(map(lambda x, y: x + '-' + str(y), lista_1, lista_2))

print(resultado)

# -----------------------------------------------

def concatenacion(lista_1, lista_2, conector):
    return [word1 + conector + str(word2) for (word1,word2) in zip(lista_1, lista_2)]

print(concatenacion(lista_1, lista_2, '-'))


print()
print('======================')