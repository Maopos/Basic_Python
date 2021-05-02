# Datos booleanos

print()

llueve = False

print(llueve)
print(type(llueve))

print(not llueve)

print()

if llueve:
    print('El dia esta lluvioso!!')
else:
    print('El dia esta soleado!!!')

print()

print('== Operaciones con valores Booleanos ==')

llave_1 = True
llave_2 = False

print()

print(llave_1 and llave_2)
print(llave_1 and not llave_2)
print(llave_1 or llave_2)
print(not llave_1 or llave_2)

print()

if llave_1 and llave_2:
    print('Si hay agua!!')
else:
    print('No hay agua!!')

print()

if llave_1 and not llave_2:
    print('Si hay agua!!')
else:
    print('No hay agua!!')

print()

if llave_1 or llave_2:
    print('Si hay agua!!')
else:
    print('No hay agua!!')

print()

if not llave_1 and llave_2:
    print('Si hay agua!!')
else:
    print('No hay agua!!')

print()

print('== Uso de la clase bool() ==')

x = bool(1)
print(x, type(x))
print()

x = bool(-1)
print(x, type(x))
print()

x = bool(0)
print(x, type(x))
print()