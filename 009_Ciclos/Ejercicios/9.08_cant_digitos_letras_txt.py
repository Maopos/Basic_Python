# Ejercicio 9.8: Contar la cantidad de dígitos y letras que tiene un texto.

print()

texto = input('Escribe un texto: ')

digitos = 0
letras = 0

for i in texto:
    if i.isnumeric():
        digitos += 1
    else:
        letras += 1

print('Digitos: ', digitos)
print('Letras: ', letras)

print()