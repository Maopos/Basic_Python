# Ejercicio 9.8: Contar la cantidad de dígitos y letras que tiene un texto.

print()

texto = input('Escribe un texto: ')
print()

digitos = 0
letras = 0
spaces = 0
otros = 0


for i in texto:
    if i.isnumeric():
        digitos += 1
    elif i.isalpha():
        letras += 1
    elif i.isspace():
        spaces += 1
    else:
        otros += 1
        
print('Caracteres: ', len(texto))
print('Digitos: ', digitos)
print('Letras: ', letras)
print('Espacios: ', spaces)
print('Otros: ', otros)

print()