# Ejercicio 9.2: Capturar una palabra o frase del usuario e invertirla.

print()

frase = input('Escribe una frase o palabra: ')

print('\nTu frase es: ', frase)

print()

print('=== Solucion 1. ===')

resultado = ''

for i in range(len(frase) -1, -1, -1):
    resultado += frase[i]

print('Tu frase invertida es: ', resultado)

print()

print('=== Solucion 2. ===')

frase_inv = frase[::-1]

print('Tu frase invertida es: ', frase_inv)


print()