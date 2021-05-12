# Acceso de elementos de una lista

print('======================')
print()

lenguajes = ['Python', 'C#', 'Html', 'Css', 'Java', 'C', 'JavaScript']

print('Cantidad de lenguajes: ', len(lenguajes))
print('Primer elemento: ', lenguajes[0])
print()

indice = 7
try:
    print('Ultimo elemento: ', lenguajes[indice])
except IndexError:
    print('El indice %i no existe...' % indice)

print('Terminó el programa.')



print()

print('=== Intento de acceso a indices negativos ===')

indice = -8

try:
    print('Ultimo elemento: ', lenguajes[indice])
except:
    print('El indice %i no existe...' % indice)
    

print()
print('======================')