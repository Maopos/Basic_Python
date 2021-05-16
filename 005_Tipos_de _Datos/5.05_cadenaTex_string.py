# Tipo de dato compuesto string

print()

nombre = 'Mauricio'
apellido = 'Posada'
email = "maopos@icloud.com"
direccion = '''
Urbanización Maracay Mz g C 14
Dosquebradas - Risaralda
Colombia.'''

print(type(nombre))
print()
print(nombre, apellido, direccion)
print()

# Interpolacion
mensaje = f'Bienvenido {nombre} {apellido}, le enviaremos la información al correo {email}.'

print(mensaje)
print()

# formato con %
mensaje = 'Bienvenido %s %s, le enviaremos la información al correo %s.' %(nombre, apellido, email)

print(mensaje)

print()

# Inmutabilidad de las cadenas

lenguaje = 'Python'

print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

lenguaje = 'p' + lenguaje[1:]
print(lenguaje)

print()

# Los elementos inmutables son estaticos

print(id('python'))
print(id('python') == id ('python'))

lenguaje = 'Python'.lower()
print(lenguaje)

print()

# Metodo split


print('=== # Metodo split ===')



print()

colores = 'Amarillo Azul Rojo Verde'
lista_colores = colores.split(' ')

print('Cantidad de elelmentos: ', len(lista_colores))

print(lista_colores)
print()

for n in lista_colores:
    print(n)

print()

# Metodo Find

indice = colores.find('Azul')
print(indice) # Busca la posicion de Azul

print()

# Creacion metodo personalizado

def encontrar(arreglo, caracter):
    j = -1
    for i in range(0, len(arreglo)):
        if caracter == arreglo[i]:
            j = i
            break

    return j

resultado = encontrar(lista_colores, 'Rojo')
print(resultado)


print()