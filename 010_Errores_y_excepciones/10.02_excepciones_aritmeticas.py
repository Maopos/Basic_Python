# Gestion de excepciones en operaciones aritmeticas



print('======================')
print()

# Capturar dividendo.

while True:
    try:
        dividendo = float(input('Escribe el dividendo: '))
        break
        
    except:
        print('** El dividendo debe ser un numero!!!.\n')

# Capturar divisor.

while True:
    try:
        divisor = float(input('Escribe el divisor: '))
        if divisor > 0:
            break
        else:
            print('** El divisor debe ser mayor a cero!!!.\n')
    except:
        print('** El divisor debe ser un numero!!!.\n')


resultado = round((dividendo / divisor), 2)



print(f'El resultado de dividir {dividendo} entre {divisor} es: {resultado}.')


print()
print('======================')