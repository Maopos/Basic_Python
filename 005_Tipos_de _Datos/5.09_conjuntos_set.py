print()

print('== Creacion de un conjunto ==')

conjunto_1 = {'Juan', 'Oliva', 'Eduard', 'Daniela', 'Juan', 'Juan', 'German'}

conjunto_2 = set(['Juan', 'Oliva', 'Eduard',
                 'Daniela', 'Juan', 'Juan', 'German'])

print('Contenido conjunto_1: ', conjunto_1)
print('Tipo de dato de conjunto_1: ', type(conjunto_1))
print('Cantidad de elementos conjunto_1: ', len(conjunto_1))
print()

print('Contenido conjunto_2: ', conjunto_2)
print('Tipo de dato de conjunto_2: ', type(conjunto_2))
print('Cantidad de elementos conjunto_2: ', len(conjunto_2))

print()


print('== Creacion de un conjunto con cadenas de caracteres ==')

frase = 'Python es un lenguaje de programación'
caracteres = set(frase)
print('Contenido caracteres: ', caracteres)
print('Tipo de dato de caracteres: ', type(caracteres))
print('Cantidad de elementos caracteres: ', len(caracteres))

print()

print('== Creacion de un conjunto a partir de una tupla ==')

primos = (2, 3, 5, 7, 7, 13, 11, 19, 2, 5, 7, 2)
print('Contenido primos: ', primos)
print('Cantidad de elementos primos: ', len(primos))
print('Tipo de datos primos: ', type(primos))

print()

grupo = set(primos)
print('Contenido grupo: ', grupo)
print('Cantidad de elementos grupo: ', len(grupo))
print('Tipo de datos grupo: ', type(grupo))

print()

print('== Conjunto colores del Arco iris ==')

arco_iris = {'Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul', 'Añil'}
print('Contenido arco_iris: ', arco_iris)
print('Cantidad de elementos arco_iris: ', len(arco_iris))
print('Tipo de datos arco_iris: ', type(arco_iris))

print()

print('== Agregar elementos a un conjunto - add() ==')

arco_iris.add('Violeta')
print('Contenido arco_iris: ', arco_iris)
print('Cantidad de elementos arco_iris: ', len(arco_iris))
print('Tipo de datos arco_iris: ', type(arco_iris))

print()

print('== Iteracion - for ==')

for i in arco_iris:
    print(i)

print()

print('== Iteracion - enumerate ==')

for i, c in enumerate(arco_iris):
    print(f'{i}: {c}')

print()

print('== Pertenencia ==')

color = 'Gris'
resultado = color in arco_iris

print(f'El color {color} pertenece a arco_iris? {resultado}' )

print()

print('== Operacion de Subconjunto ==')

colores = {'Rojo', 'Verde', 'Azul', 'Gris', 'Negro'}
resultado = colores.issubset(arco_iris)

print('El conjunto {} es subconjunto de arco_iris?: {}'.format(colores, colores.issubset(arco_iris)))

print()

print('== Operacion de Union ==')

union_colores = arco_iris.union(colores)

print('Contenido union_colores: ', union_colores)
print('Cantidad de elementos union_colores: ', len(union_colores))
print('Tipo de datos union_colores: ', type(union_colores))

print()

print('== Operacion de Interseccion ==')

comunes = arco_iris.intersection(colores)
print('Contenido comunes: ', comunes)
print('Cantidad de elementos comunes: ', len(comunes))
print('Tipo de datos comunes: ', type(comunes))

print()


print('== Operacion de Superconjunto ==')

rgb = {'Verde', 'Azul', 'Rojo'}
resultado = arco_iris.issuperset(rgb)
print('El conjunto {} es superconjunto de {}?: {}'.format(arco_iris, rgb, resultado))

print()


print('== Operacion Resta ==')

diferencia = colores - arco_iris
print('La diferencia entre colores y arco_iris es: ', diferencia)
print('Cantidad de elementos diferencia: ', len(diferencia))
print('Tipo de datos diferencia: ', type(diferencia))

print()

diferencia = arco_iris - colores
print('La diferencia entre arco_iris y colores es: ', diferencia)
print('Cantidad de elementos diferencia: ', len(diferencia))
print('Tipo de datos diferencia: ', type(diferencia))

print()

print('== Operacion de diferencia simetrica ==')

diferencia_simetrica = arco_iris.symmetric_difference(colores)
print('La diferencia_simetrica entre arco_iris y colores es: ', diferencia_simetrica)
print('Cantidad de elementos diferencia_simetrica: ', len(diferencia_simetrica))
print('Tipo de datos diferencia_simetrica: ', type(diferencia_simetrica))

print()

print('== Remover Elementos de un conjunto ==')

colores.remove('Negro')
print('Contenido colores: ', colores)
print('Cantidad de elementos colores: ', len(colores))
print('Tipo de datos colores: ', type(colores))

print()

print('== Remover Elementos de un conjunto al azar ==')

color = colores.pop()
print('Se elimino el color: ', color)
print('Contenido colores: ', colores)
print('Cantidad de elementos colores: ', len(colores))
print('Tipo de datos colores: ', type(colores))

print()

print('== Remover Todos Elementos de un conjunto ==')

colores.clear()
print('Contenido colores: ', colores)
print('Cantidad de elementos colores: ', len(colores))
print('Tipo de datos colores: ', type(colores))

print()