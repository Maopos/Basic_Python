# Argumentos por defecto en una funcion.

print('======================')
print()

def saludar(nombre, saludo = 'Hola', pais = 'Colombia'):
    '''
    Saluda utilizando un nombre y un pais
    
    Parameters:
    nombre: Nombre de la persona
    saludo: Tipo de saludo
    pais: Pais de procedencia, Nacionalidad
    
    Returns:
    Una frase con el saludo que incluye nombre y nacionalidad
    '''
    frase = f'{saludo}, mi nombre es {nombre}, y soy de {pais}.'

    return frase

print(saludar('Mauricio'))
print(saludar('Natalia', 'Buenas Tardes'))
print(saludar('Carolina', pais='Brasil'))

print()

print('=== Ejemplo 2 ===')



print()

def exponenciacion(base, exponente = 2):
    '''
    Calcula la exponenciacion de un numero base respecto a un exponenete
    
    Parameters:
    base: Numero a exponenciar
    exponente: Potencia de la exponenciacion, deafult = 2
    
    Returns:
    Numero (base) elevado a una potencia(exponente).
    '''
    resultado = base ** exponente

    return resultado

potencia = exponenciacion(5)
print('El resultado es: ', potencia)

potencia = exponenciacion(5, 3)
print('El resultado es: ', potencia)

print('\n======================')