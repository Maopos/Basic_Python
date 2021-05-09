# Ejercicio 8.1. Capturar la temperatura (sea en grados Celcius o Fahrenheit) y convertirla a la escala contraria.

print()

temperatura = float(input('Ingrese la temperatura: '))
tipo = float(input('Si son grados Celsius escriba 1, si son grados Fahrenheit escriba 2: '))

while tipo < 1 or tipo > 2:
    tipo = int(input('Si son grados Celsius escriba 1, si son grados Fahrenheit escriba 2: '))
    
print('==========\n')

if tipo == 1:
    calculo = temperatura * 9 / 5 + 32
    print(f'{temperatura}ºC es igual a {calculo}ºF.')
else:
    calculo = (temperatura - 32) * 5/9
    print(f'{temperatura}ºF es igual a {calculo}ºC.')
    



print()