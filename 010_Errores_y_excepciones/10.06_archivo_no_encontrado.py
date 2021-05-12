# Error al abrir archivo

print('======================')
print()

print('=== Error al abrir archivo ===\n')

archivo = 'python.txt'

try:
    with open(archivo, 'r') as f:
        for i in f.readlines():
            print(i)
except FileNotFoundError as e:
    print('Error: ', e, 'Este archivo no existe...')



print()



print()
print('======================')