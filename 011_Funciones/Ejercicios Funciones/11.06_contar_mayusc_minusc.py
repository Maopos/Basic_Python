# Ejercicio 11.6: Usar una función para contar minúsculas y mayúsculas en una cadena.

print('======================')
print()

def contar_May_min(texto):
    if isinstance(texto, str):
        minusculas = 0
        mayusculas = 0
        

        for i in texto:
            if i.isalpha():
                if i.islower():
                    minusculas += 1
                elif i.isupper():
                    mayusculas += 1
                
        return minusculas, mayusculas

    else:
        raise TypeError('El argumento debe ser texto.')


frase = 'Hola Buenos Dias AMOR!! 123'

frase2 = 1231234

frase3 = ['Hola', 'Como', 'Estas?']


try:
    resultado = contar_May_min(frase)
    print(f'En el texto "{frase}" se encontraron {resultado[0]} minusculas y {resultado[1]} Mayusculas.')
except TypeError as e:
    print('Error: ', e)

print()
print('======================')