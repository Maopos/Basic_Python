# Pasar argumentos por valor y referencia

print('======================')
print()



print('=== Pasar argumentos por valor ===')
print()

def duplicar(numero):
    numero *= 2
    print('El numero duplicado es igual a : ', numero)

x = 2

print('Valor inicial de x: ', x)

duplicar(x)

print('Valor inicial de x: ', x)


print()

print('=== Pasar argumentos por referencia ===\n')

def agregarElemento (lista):
    lista.append(2)

numeros = [0, 1]

print('Numeros: ', numeros)

agregarElemento(numeros)

print('Numeros: ', numeros)

print()
print('======================')