# Tipo de dato compuesto diccionario

print()

print('== Creacion de diccionarios ==')

diccionario_1 = {'prop1': 1, 'prop2': 'dos', 'prop3': [1, 2, 3]}


diccionario_2 = dict()
diccionario_2['prop1'] = 1
diccionario_2['prop2'] = 'dos'
diccionario_2['prop3'] = [1, 2, 3]


print('dict__1', diccionario_1)
print(type(diccionario_1))
print('dict__2', diccionario_2)
print(type(diccionario_2))

print()

computador = {'Id': 1876567, 'Marca': 'Msi', 'Ram': 128, 'Cpu': 'M1', 'Almacenamiento': 256}
print(computador)
print(f'Computador tiene {len(computador)} propiedades.')
print('Tipo de dato de Computador es: ', type(computador).__name__)

print()

print('== Acceso a las propiedades y valores de un diccionario ==')
print(f'Id: {computador["Id"]}')
print(f'Marca: {computador["Marca"]}')
print(f'Memoria RAM: {computador["Ram"]} Gb')
print(f'CPU: {computador["Cpu"]}')
print(f'Almacenamiento: {computador["Almacenamiento"]} Gb')

print()

print('== Modificacion del contenido de un diccionario. ==')

computador['Marca'] = 'Apple'
computador['Id'] = 7865875
computador['Gpu'] = '8 Nucleos'
print(computador)
print(f'Computador tiene {len(computador)} propiedades.')

print()

print('== Iterar un diccionario - key ==')

for k in computador.keys():
    print(k.upper(), ': ', computador[k])

print()

print('== Iterar un diccionario - values() ==')

for v in computador.values():
    print(v)

print()

print('== Iterar un diccionario - keys y values() - items() ==')

for k, v in computador.items():
    print(k, ': ', v)

print()

print('== Metodos y operadores para diccionarios ==')
print('List() - convierte los atributos en una lista')
atributos = list(computador)
print(atributos)
print('Cantidad de atributos de computador: ', len(atributos))

print()
print('in - buscar en un diccionario')
print('Gpu' in computador)

print()
print('pop - extrae un elemento del dict')

valor = computador.pop('Ram')
print(computador)
print(f'Se ha removido la key {valor}')

valor = computador.pop('Ram', 'No disponible')
print(valor)

print()
print('popitem() - remueve y retorna una (key, value)')

atributo = computador.popitem()

print(atributo)
print(computador)

print()
print('reversed(d) - retorna el dict en orden inverso')

print(computador)
print(list(reversed(computador)))

print()

for k in (computador):
    print(f'{k}: {computador[k]}')

print()

for k in reversed(computador):
    print(f'{k}: {computador[k]}')

print()

print('Remover elementos de un diccionario - clear()')

print('Cantidad de llaves de computador', len(computador))
computador.clear()
print(computador)
print()