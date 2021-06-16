''' Problema #5:
Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate. '''

print('======================')
print()

listado = [120, 130, 140, 150, 160, 170]

diccio = {}
for v, k in enumerate(listado):
    diccio[k] = v

print(diccio)

# -----------------------------------

def crear_dict(iterable):
    return {key: value for value, key in enumerate(iterable)}

print(crear_dict(listado))
    

print()
print('======================')