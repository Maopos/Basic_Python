# Ejercicio 5.14: Calcular la diferencia entre dos conjuntos.

print()

aula_1 = {'Juan', 'Oliva', 'Eduard', 'Daniela', 'Juan', 'Andres', 'German'}

aula_2 = {'Juan', 'Mauricio', 'Eduard', 'Daniel', 'Juan', 'Libardo', 'German'}

print('Estudiantes del Aula 1: ', aula_1)
print('Estudiantes del Aula 2: ', aula_2)
print('====================================\n')

diferentes = aula_1.difference(aula_2)

print('La diferencia entre Aula 1 y Aula 2 es:', diferentes)

diferentes = aula_2.difference(aula_1)

print('La diferencia entre Aula 2 y Aula 1 es:', diferentes)

print()