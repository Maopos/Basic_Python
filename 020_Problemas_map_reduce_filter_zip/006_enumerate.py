''' Problema #6:
Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice. Utilizar la función enumerate. '''

print('======================')
print()

lista = [0,2,2,1,5,5,6,10]

recuento = []
for k, v in enumerate(lista):
    if k == v:
        recuento.append(v)

print(len(recuento))


# ----------------------------------

cuantos = len([num for count, num in enumerate(lista) if count == num])

print(cuantos)

# ----------------------------------

cantidad_iguales = len([k for k, v in enumerate(lista) if k == v])

print(cantidad_iguales)

print()
print('======================')