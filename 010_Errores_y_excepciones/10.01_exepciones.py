# Excepciones en el flujo de ejecucion de python

print()

try:
    numero = int(input('Escriba un numero entero: '))
    print('Tu numero es: ', numero)
    print('Su tipo es: ', type(numero))

except ValueError as e:
    print('Error:', e)


print()
print('El programa ha terminado.')
print()

print('=== Captura de un numero entero ===\n')

while True:
    try:
        edad = int(input('Cual es su edad: '))
        if edad > 0:
            if edad <= 70:
                break
            else:
                print('** Debes tener menos de 70 años.\n')
        else:
            print('** Debe ser numero positivo.\n')
    except:
        print('** La edad debe ser un numero.\n')

print('\nSu edad es: ', edad, 'años.')

print()
