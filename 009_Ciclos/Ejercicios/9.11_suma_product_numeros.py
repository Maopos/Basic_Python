# Ejercicio 9.11: Solicitar al usuario una cantidad arbitria de valor numéricos y luego calcular su suma y productoria.

print()

cantidad = int(input('Cuantos numeros deseas ingresar?: '))
print()

suma = 0
producto = 1
num = 1

for i in range(cantidad):
    numero = float(input(f'Escribe el {num}º numero: '))
    suma += numero
    producto *= numero
    num += 1

print()
print('La suma es: ', suma)
print('El producto es: ', producto)

print()