# Ejercicio 5.13: Realizar operaciones de unión e intersección de conjuntos.

print()

aula_1 = {'Juan', 'Oliva', 'Eduard', 'Daniela', 'Juan', 'Andres', 'German'}

aula_2 = {'Juan', 'Mauricio', 'Eduard', 'Daniel', 'Juan', 'Libardo', 'German'}

print('Estudiantes del Aula 1: ', aula_1)
print('Estudiantes del Aula 2: ', aula_2)
print('====================================\n')

comunes = aula_1.intersection(aula_2)
todos = aula_1.union(aula_2)

print('Listado de todos los estudiantes: ', todos)
print('Total de estudiantes: ', len(todos))
print('Estudiantes que estudian en ambas Aulas: ', comunes)
print('====================================\n')

print()