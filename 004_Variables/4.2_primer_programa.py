def sumar(a, b):
    suma = a + b
    return suma

num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))

resultado = sumar(num1, num2)

print('La suma de {} y {} es: {}.'.format(num1,num2,resultado))