def sumar(a, b):
    suma = a + b
    return suma

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

resultado = sumar(num1, num2)

print('La suma de {} y {} es: {}.'.format(num1,num2,resultado))