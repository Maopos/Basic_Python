# Ejercicio 11.10: Crear una función recursiva para dividir dos números.

print('======================')
print()

def dividir(dividendo, divisor):
    if divisor == 0:
        raise ValueError('No es posible la division por cero (0).')
    elif dividendo == divisor:
        return 1
    elif dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)

num_1 = 1
num_2 = 0

try:
    resultado = dividir(num_1, num_2)
    print(f'La division de {num_1} entre {num_2} es igual a {resultado}')
except ValueError as e:
    print('Error: ', e)

print()
print('======================')