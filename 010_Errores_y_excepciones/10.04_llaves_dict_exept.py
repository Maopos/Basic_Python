# Excepciones con diccionarios

print('======================')
print()

versiones = {'Python': '3.9.4', 'Java': '12', 'JavaScript': 'ES6', 'C#': '8'}

lenguaje = input('Escriba un lenguaje: ')

try:
    version = versiones[lenguaje]

    print(f'La version actual de {lenguaje} es {version}.')

except KeyError as e:
    print('Error: ', e)

print('Fin del programa.')
print()

print('=== Get() ===')



print()

version = versiones.get('java', '1.0.0')
print(f'La version actual de java es {version}.')

print()
print('======================')