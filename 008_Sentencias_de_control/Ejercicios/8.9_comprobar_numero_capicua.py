# Ejercicio 8.9. Comprobar si un número es capicúa.

print()

numero = int(input('Escriba un numero: '))

while numero < 0:
    numero = int(input('Escriba un numero: '))

if str(numero) == str(numero)[::-1]:
    print(f'El numero {numero} es capicua.')
else:
    print(f'El numero {numero}  NO es capicua.')



print()