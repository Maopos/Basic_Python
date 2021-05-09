# Uso de condicionales para verificar si un numero es mayor a otro

print()

num_1 = int(input('Escriba un primer numero: '))
num_2 = int(input('Escriba un segundo numero: '))
print('==\n')

if num_1 > num_2:
    print('El numero {} es mayor a {}.'.format(num_1, num_2))
elif num_1 < num_2:
    print('El numero {} es mayor a {}.'.format(num_2, num_1))
else:
    print('El numero {} es igual a {}.'.format(num_2, num_1))
    
    

print()