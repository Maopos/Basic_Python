# Ejercicio 11.3: Crear una función para multiplicar todos los números en una lista o tupla.

print('======================')
print()

numeros = (2, 45, 32, 76, 41, 98, 100)

vacio = ()

numero = 100

def multiplicar(tupla):
    if isinstance(tupla, (list, tuple)):
        producto = 1
        if len(tupla) > 0:
            for i in tupla:
                producto *= i
        else:
            producto = None
        
        return producto
    else:
        raise ValueError('No se pueden utilizar argumentos diferentes a Listas o tuplas.')



try:
    resultado = multiplicar(vacio)
    if resultado:
        print('El producto de multiplicar los elementos de la tupla es: ', resultado)
    else:
        print('La lista o tupla esta vacia.')
except ValueError as e:
    print('Error: ', e)





print()
print('======================')