# Ejercicio 5.2: Invertir el contenido de una tupla.

print()

animales = ('1_Perro', '2_Caballo', '3_Oveja', '4_Gato', '5_Paloma')

print(animales)

print()

animales_invertidos = []
print('== Metodo for ==')
for i in range(len(animales)-1, -1, -1): # empieza en len -1, hasta -1, decreciendo en -1
    animales_invertidos.append(animales[i])

animales_invertidos = tuple(animales_invertidos)

print(animales_invertidos)

print()

print('== Metodo convertir a list - reverse - tuple ==')

animales = list(animales)

animales.reverse()

animales = tuple(animales)

print(animales)

print()