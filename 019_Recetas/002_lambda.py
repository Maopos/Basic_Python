print('======================')
print()

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x*x, numeros))

print(cuadrados)

funcion = lambda x: x*x

cuadrados_con_funcion_en_una_variable = list(map(funcion, numeros))

print(cuadrados_con_funcion_en_una_variable)


print()
print('======================')