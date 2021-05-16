# Ejercicio 11.7: Tomar una lista de números e identificar los números únicos.

print('======================')
print()

def buscar_numeros_unicos(lista):
    if isinstance(lista, (list, tuple)):
        unicos = []
        for i in lista:
            if i not in unicos:
                unicos.append(i)

    else:
        raise TypeError('El argumento debe ser de tipo Lista o Tupla.')
    
    return sorted(unicos)


numeros = [1, 13, 3, 4, 5, 65, 5, 3, 44, 7, 6, 2 ,400, 1, 9, 7, 8, 5, 4]

listado = 'Hola'

diccio = {'werwe': 234, 'sdf': 5435}

try:
    resultado = buscar_numeros_unicos(numeros)
    print('El listado de numeros unicos es: ', resultado)
except TypeError as e:
    print('Error: ', e)

print()
print('======================')