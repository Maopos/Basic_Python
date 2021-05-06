# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.

print()

paises = ['Argentina', 'Peru', 'Colombia', 'Irak', 'Alemania', 'China', 'Iran']

print(paises)
print('Cantidad de elementos: ', len(paises))

print()

print('== Solucion 1 - for ==')

paises_5_chart = []

for i in paises:
    if len(i) >= 5:
        paises_5_chart.append(i)

print(paises_5_chart)
print('Cantidad de elementos: ', len(paises_5_chart))

print()
       
print('== Solucion 2 ==')

paises_5_chart = [i for i in paises if len(i) >= 5]

print(paises_5_chart)
print('Cantidad de elementos: ', len(paises_5_chart))

print()