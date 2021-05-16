def sumar(a, b):
    '''
    Suma dos numeros
    
    Parameters:
    a: primer numero
    b: segundo numero
    
    Returns:
    Suma de ambos numeros
    '''
    return a + b



def restar(a, b):
    '''
    Resta dos numeros
    
    Parameters:
    a: primer numero
    b: segundo numero
    
    Returns:
    Resta de ambos numeros
    '''
    return a - b



def multiplicar(a, b):
    '''
    Multiplica dos numeros
    
    Parameters:
    a: primer numero
    b: segundo numero
    
    Returns:
    Multiplica de ambos numeros
    '''
    return a * b



def dividir(a, b):
    '''
    Divide dos numeros
    
    Parameters:
    a: dividendo
    b: divisor
    
    Returns:
    Division del dividendo entre el divisor
    '''

    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError('No es posible dividir entre cero (0)')