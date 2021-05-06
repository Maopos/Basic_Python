# Ejercicio 5.15: Calcular la diferencia simétrica entre dos conjuntos.

print()

aula_1 = {'Juan', 'Oliva', 'Eduard', 'Daniela', 'Juan', 'Andres', 'German'}

aula_2 = {'Juan', 'Mauricio', 'Eduard', 'Daniel', 'Juan', 'Libardo', 'German'}

print('Estudiantes del Aula 1: ', aula_1)
print('Estudiantes del Aula 2: ', aula_2)
print('====================================\n')

diferentes = aula_1.symmetric_difference(aula_2)

print('La diferencia simetrica entre Aula 1 y Aula 2 es:', diferentes)

print()