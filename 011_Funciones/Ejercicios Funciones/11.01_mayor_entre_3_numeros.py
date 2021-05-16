# Ejercicio 11.1: Crear una función para obtener el mayor de tres números.

print('======================')
print()

def mayorEntreTres(a, b, c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
    
x = 1
y = 10
z = 10
          

mayor = mayorEntreTres(x, y, z)

print(f'El número mayor entre {x}, {y} y {z} es: {mayor}.')
        

print()
print('======================')