# Ejercicio 11.8: Crear una función recursiva para sumar los números de una lista.

print('======================')
print()

def sumar(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar(lista[1:])



numeros = [1, 2, 3, 4, 5]

resultado = sumar(numeros)

print('La suma es igual a:', resultado)

print()
print('======================')