# Ejercicio 5.10: Remover todos los elementos duplicados de un diccionario.

print()

articulos = {1001: 'Mouse', 1002: 'Teclado', 1003: 'Monitor', 1004: 'Mouse', 1005: 'audifonos', 1006: 'Teclado'}

print('Articulos: ', articulos)
print('Cantidad de Articulos: ', len(articulos))
print('========================================\n')

unicos = {}

for i, v in articulos.items():
    if v not in unicos.values():
        unicos[i] = v

print('Articulos Unicos: ', unicos)
print('Cantidad de Articulos Unicos: ', len(unicos))
print('========================================\n')

print()