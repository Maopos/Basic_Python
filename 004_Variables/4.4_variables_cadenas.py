nombre = 'Mauricio'
apellido = 'Posada'
nombre_completo = nombre + ' ' + apellido

print()

print('Nombre: ', nombre)
print('Apellido: ', apellido)
print('Nombre Completo: ', nombre_completo)

print()

print('Tipo de dato de la variable nombre:', type(nombre))
print('Tipo de dato de la variable apellido:', type(apellido))

print()

edad = 40

print(nombre_completo, 'tiene', edad, 'años.')

#Solo se concatenan caracteres del tipo string
nombre_completo = nombre_completo + ' tiene ' + str(edad) + ' años.'
print(nombre_completo)

presentacion = '{} {} tiene {} años.'.format(nombre, apellido, edad)
print(presentacion)

print()