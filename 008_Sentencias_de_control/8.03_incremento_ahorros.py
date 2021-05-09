# Realizar aumento sobre los ahorros dependiendo de la cantidad ahorrada

print()

ahorro = float(input('Digite su cantidad ahorrada: '))

if ahorro > 0:
    if ahorro < 1000000:
        ahorro *= 1.1
    elif ahorro < 3000000:
        ahorro *= 1.07
    elif ahorro < 10000000:
        ahorro += 1.05
    else:
        ahorro *= 1.03
    
    print('El ahorro se ha incrementado a {}'.format(ahorro))

else:
    print('Cantidad negativa o igual a cero.')

print('Programa finalizado')

print()