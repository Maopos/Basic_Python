# Entrada de datos - input()

print()

print('Entrada de datos - input()')
print('===============\n')

try:
    nombre = input('Cual es su nombre: ')

    print('Buenos dias', nombre + '!!')
    print('Tipo de dato: ', type(nombre))
except EOFError:
    print('\nEl usuario cancelo el proceso.')

print('Proceso terminado con exito.')



print()
