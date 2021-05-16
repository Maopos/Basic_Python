# Ejercicio 11.9: Crear una función recursiva para comprobar si una cadena es palíndromo.

print('======================')
print()

def comprobar_palindromo(texto):
    if len(texto) < 1:
        return 'Si es Palíndromo'
    else:
        if texto[0] == texto[-1]:
            return comprobar_palindromo(texto[1:-1])
        else:
            return 'No es Palíndromo'


palabra = 'lateleletal'

palabra2 = 'Elcaminonimacle'

resultado = comprobar_palindromo(palabra2)
print(f'La palabra "{palabra2}" {resultado}')

print()
print('======================')