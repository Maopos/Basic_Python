'''
Ejercicio 8.7. Categorizar según la cantidad de puntos obtenidos por un jugador.

+----------+---------------+
| Puntos   | Categoría     |
+----------+---------------+
| 0-100    | Principiante  |
+----------+---------------+
| 101-500  | Estándar      |
+----------+---------------+
| 501-2000 | Experimentado |
+----------+---------------+
| 2000>    | Máster        |
+----------+---------------+
'''

print()

puntos = int(input('Digite su puntuación: '))

while puntos < 0:
    puntos = int(input('Digite su puntuación: '))

if 0 <= puntos <= 100:
    print('Su categoria es Principiante.')
elif 101 < puntos <= 500:
    print('Su categoria es Estandar.')
elif 501 < puntos <= 2000:
    print('Su categoria es Experimentado.')
else:
    print('Su categoria es Master.')

print()