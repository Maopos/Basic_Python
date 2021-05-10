# Ejercicio 9.3: Generar los primeros 50 números de la serie Fibonacci.

print()

print('=== Serie Fibonacci. ===')

print()

serie = []
num = 1
digitos = int(input('Escribe cuantos numeros quieres obtener: ')) - 1

print()

i = 0
while i <= 1:
    serie.append(i)
    break
while i < digitos:
    if num == 1:
        serie.append(1)
    else:
        serie.append(num)
    num += serie[i]
    i += 1

print(serie)



print()
