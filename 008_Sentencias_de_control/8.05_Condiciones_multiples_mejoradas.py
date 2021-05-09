# Evaluacion de condiciones multiples.

print()

numero = int(input('Escriba un numero: '))
print()

# a <= x <= b

if numero % 5 == 0 and 20 <= numero <= 40:
    print('El numero {} es divisible entre 5 y se halla entre 20 y 40.'.format(numero))
else:
    print('El numero no cumple los requerimientos.')

print()