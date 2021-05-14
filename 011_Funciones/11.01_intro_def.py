# Introduccion a funciones

print('======================')
print()

print('=== Creacion de funciones ===\n')


def sumar(num_1, num_2):
    '''
    Suma dos numeros int o float

    Parameters:
    num_1: numero 1
    num_2: numero 2

    Returns:
    Suma de num_1 + num_2
    '''
    suma = num_1 + num_2
    return suma


x = 2
y = 3

resultado = sumar(x, y)

print(f'La suma de {x} y {y} es igual a: ', resultado)


print()

# print('=== Obtener documentacion ayuda de una funcion ===')

 # help(sumar)


print()

print('=== Intercambiar los valores de las variables ===')

def intercambiarValores (a, b):
    '''
    Intercambia los valores de 2 variables.
    
    Parameters:
    a: primer valor
    b: segundo valor
    
    Returns:
    Los valores de a y b intercambiados.
    '''
    auxiliar = a
    a = b
    b = auxiliar

    return a, b

x = 2
y = 3
print('Valores originales de X y Y')
print(f'x = {x} *** y = {y}')

resultado = intercambiarValores(x, y)

x = resultado[0]
y = resultado[1]

print('Valores finales de X y Y')
print(f'x = {x} *** y = {y}')


print()

print('=== Funciones por defecto de Python ===')

x, y = y, x

print('Valores Originales de X y Y')
print(f'x = {x} *** y = {y}')

print()
print('======================')
