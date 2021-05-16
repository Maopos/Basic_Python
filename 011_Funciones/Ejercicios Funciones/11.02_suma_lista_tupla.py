# Ejercicio 11.2: Crear una función para sumar todos los números en una lista o tupla.

print('======================')
print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

precios = (999.9, 59.9, 27.5)

nombre = 'Mauricio Posada'

def sumar(valores):
    '''
    Suma los valores de una lista o tupla
    
    Parameters:
    valores de la lista o tupla
    
    Returns:
    Resultado de la suma de los valores de una lista o tupla.
    '''
    if isinstance(valores, (list, tuple)):
        acumulado = 0

        for i in valores:
            acumulado += i

        return acumulado
    else:
        raise ValueError('El argumento debe ser una lista o una tupla.')


try:
    resultado = sumar(precios)
    print('El resultado de la suma de los elementos de la lista es: ', resultado)
    resultado = sumar(numeros)
    print('El resultado de la suma de los elementos de la lista es: ', resultado)
    resultado = sumar(nombre)
    print('El resultado de la suma de los elementos de la lista es: ', resultado)
except ValueError as e:
    print('Error: ', e)



print()
print('======================')