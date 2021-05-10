# Ejercicio 9.4: Calcular el factorial de un número dado por el usuario.

print()

numero = int(input('Escribe un numero entero positivo: '))

while numero < 0:
    numero = int(input('Escribe un numero entero positivo: '))



factorial = 1


if numero == 0 or numero == 1:
    factorial = 1
else:
    for i in range(1, numero + 1):
        factorial *= i

print(f'El Factorial de {numero} es {factorial}.')


print()