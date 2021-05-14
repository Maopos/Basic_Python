# Lista variable de argumentos de una funcion

print('======================')
print()

# def sumar (a, b):
#     return a + b

# def sumar (a, b, c):
#     return a + b + c

# def sumar (a, b, c, d):
#     return a + b + c + d


def sumar(*valores):
    suma = 0

    for v in valores:
        suma += v
    
    return suma

resultado = sumar(1)

print('Suma: ', resultado)
print()

resultado = sumar(1, 2)

print('Suma: ', resultado)
print()

resultado = sumar(1, 2, 3)

print('Suma: ', resultado)
print()

print()
print('======================')