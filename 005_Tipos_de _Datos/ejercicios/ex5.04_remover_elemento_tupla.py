# Ejercicio 5.4: Remover un elemento (valor) de una tupla.

print()

nombres = ('Mauricio', 'Jennifer', 'Veronica', 'Sarita', 'Violeta')

print(nombres)
print('Cantidad de elementos: ', len(nombres))


print()

borrado = input('Que nombre quieres borrar?: ')

posicion = nombres.index(borrado)

if borrado in nombres:
    # Las tuplas no se pueden modificar
    nombres = nombres[0:posicion] + nombres[posicion + 1:]

    print()

    print(nombres)
    print('Cantidad de elementos: ', len(nombres))

else:
    print('No encontrado')

print()