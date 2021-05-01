'''
Ejercicio 4.2: Mostrar en pantalla fecha y hora actuales del sistema
'''

import datetime

print()

ahora = datetime.datetime.now()

print('Fecha y hora actual: ', ahora)
print(type(ahora))

ahora_formato = ahora.strftime('%H:%M:%S %Y-%m-%d')
print(ahora_formato)

print()

