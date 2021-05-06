# Ejercicio 5.12: Convertir un diccionario en su representación en el formato JSON.

import json

print()

edades = {'Mauricio': 40, 'Stella': 64, 'Jennifer': 34, 'Sarita': 12, 'Violeta': 8, 'Daniel': 35, 'Libardo': 37}

print('Edades: ', edades)
print('Tipo de dato de edades: ', type(edades).__name__)
print('========================================\n')

edades_json = json.dumps(edades)
print('Edades en Json: ', edades_json)
print('Tipo de dato de edades en Json: ', type(edades_json).__name__)
print('========================================\n')


print()