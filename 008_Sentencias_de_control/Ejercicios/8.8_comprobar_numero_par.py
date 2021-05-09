# Ejercicio 8.8. Determinar si un número dado por el usuario es par o impar.

print()

numero = int(input('Ingrese un número: '))

if numero % 2 == 0:
    print('El número {} es par.'.format(numero))
else:
    print('El número {} es impar.'.format(numero))
    

print()