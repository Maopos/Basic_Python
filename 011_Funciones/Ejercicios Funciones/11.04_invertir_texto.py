# Ejercicio 11.4: Crear una función para invertir el contenido de una cadena de caracteres.

print('======================')
print()

cadena = 'Hola como estas...!!'

numero = 12322

def invertir(texto):
    
    if isinstance(texto, str):
        nuevo = ''

        for i in range(len(texto) -1, -1, -1):
            nuevo += texto[i]
        return nuevo
    else:
        raise TypeError('Solo se admiten cadenas de caracteres.')


try:
    resultado = invertir(cadena)
    print('Frase original: ', cadena)
    print('Frase invertida', resultado)
except TypeError as e:
    print('Error: ', e)

print()

try:
    resultado = invertir(numero)
    print('Frase original: ', numero)
    print('Frase invertida', resultado)
except TypeError as e:
    print('Frase original: ', numero)
    print('Error: ', e)

print()
print('======================')