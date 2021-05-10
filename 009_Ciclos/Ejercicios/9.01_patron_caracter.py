# Ejercicio 9.1: Construir un patrón con el carácter asterisco.

print()



print('=== Construir patron con asteriscos ===')

caracter = '* '

i = 0
while i < 3:
    print(caracter * i)
    i += 1
while i > 0:
    print(caracter * i)
    i -= 1
        
print()

for i in range(5):
    if i <= 2:
        for j in range(i + 1):
            print('*', end=' ')
    else:
        for j in range(5 - i):
            print('*', end=' ')
    print()
    


print()