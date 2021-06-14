print('======================')
print()

def sumar(parametro):
    final = list(parametro)
    
    return final


numeros = [(1, 2 ,3, 4, 5, 6), (7, 8, 9, 0, 1)]

resultado = list(map(sumar, numeros))

print(resultado)

print('\n== Pow - Potencias')

digitos = [2, 3, 4, 5]

potencias = [4, 5, 6, 7]

resultado = list(map(pow, digitos, potencias))

print(resultado)






print()
print('======================')