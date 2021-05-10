import random

print()

aleatorio = random.randint(1, 10)

intentos = 3

print('=== Adivina un numero entre 1 y 10 ===')


print()

while intentos > 0:
    numero = int(input('Digita un numero entre 1 y 10: '))
    if numero < aleatorio:
        print(f'El numero debe ser mayor a {numero}.\n')
    elif numero > aleatorio:
        print(f'El numero debe ser menor a {numero}.\n')
    else:
        print('Adivinaste!!!')
        break
    intentos -= 1

while intentos == 0:
    print('Se agotaron los intentos. Perdiste!!')
    break

print()