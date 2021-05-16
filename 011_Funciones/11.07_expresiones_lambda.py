# Expresiones Lambda - Funciones anonimas

print('======================')
print()

print('=== Expresiones Lambda - Funciones anonimas. ===')

def sumar(a, b):
    return a + b

x = 2
y = 3

print(f'La suma de {x} y {y} es igual a: {sumar(x, y)}')

sumar_lambda = lambda a, b: a + b

print(f'La suma de {x} y {y} es igual a: {sumar_lambda(x, y)}')


print()

print('=== Ejemplo 2 ===')

cuadrado_lambda = lambda n: n ** 2

numero = 9

print(f'El cuadrado de {numero} es: {cuadrado_lambda(numero)}')

print()

print('=== Filtrar el contenido de una lista ===')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Contenido de numeros: ', numeros)
print('Cantidad de elementos: ', len(numeros))

def extraer_impares(lista):
    impares = []

    for i in lista:
        if i % 2 == 1:
            impares.append(i)
    
    return impares

resultado = extraer_impares(numeros)

print('\nContenido de resultado: ', resultado)
print('Cantidad de elementos: ', len(resultado))
#impares = lambda *numeros: if numeros

resultado = [n for n in numeros if n % 2 != 0]
print('\nContenido de resultado: ', resultado)
print('Cantidad de elementos: ', len(resultado))

print()

print('=== Con funcion Lambda - filter ===')

pares = list(filter(lambda n: n % 2 == 0, numeros))
print('\nContenido de pares: ', pares)
print('Cantidad de elementos en pares: ', len(pares))

def filtro(n):
    return n % 2 == 0

pares = list(filter(filtro, numeros))
print('\nContenido de pares: ', pares)
print('Cantidad de elementos en pares: ', len(pares))

print()

print('=== Funcion map() para mapeo del contenido de una lista ===')

def elevar_cuadrados(lista):
    cuadrados = []

    for i in lista:
        cuadrados.append(i ** 2)
    
    return cuadrados

resultado = elevar_cuadrados(numeros)

print('Lista: ', numeros)
print('Los Cuadrados son: ', resultado)

resultado = [n ** 2 for n in numeros]

print('\nLista: ', numeros)
print('Los Cuadrados son: ', resultado)

resultado = list(map(lambda n: n ** 2, numeros))
print('\nLista: ', numeros)
print('Los Cuadrados son: ', resultado)

print()
print('======================')