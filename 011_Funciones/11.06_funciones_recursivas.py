# Funciones recursivas

print('======================')
print()

print('=== Funciones Recursivas ===')

# 4! = 1 * 2 * 3 * 4 = 24
# 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial_iterativo(n):
    '''
    Calcula el factorial de un numero. (Enfoque iterativo)
    
    Parameters:
    n: numero de factorial a calcular
    
    Returns:
    Factorial
    '''
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

def factorial_recursivo(n):
    '''
    Calcula el factorial de un numero. (Enfoque recursivo)
    
    Parameters:
    n: numero de factorial a calcular
    
    Returns:
    Factorial
    '''
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


resultado = factorial_iterativo(4)
print('Factorial iterativo: ', resultado)

resultado = factorial_recursivo(4)
print('Factorial recursivo: ', resultado)

print()

print('=== Funcion Fibonacci ===')

def fibonacci_iterativa(n):

    serie = []
    num = 1

    i = 0
    while i == 0:
        serie.append(i)
        break
    while i < n - 1:
        if num == 1:
            serie.append(1)
        else:
            serie.append(num)
        num += serie[i]
        i += 1          
                    
    return serie  

def fibonacci_recursiva(n):
    

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursiva(n - 2) + fibonacci_recursiva(n - 1)
        
    
    


print('Fibonacci iterativa: ', fibonacci_iterativa(10))
    
print('Fibonacci recursiva: ', fibonacci_recursiva(10))

print()

print('=== Fibonacci For ===')

def fibonacci_for(n):

    lista = [0]
    b = 1

    for i in range(n):
        if i == 0:
            lista[0] = 0
        elif i == 1:
            lista.append(1)
        else:
            lista.append(b)
        b += lista[i-1]   
        
    return lista


print(fibonacci_for(10))

print()
print('======================')