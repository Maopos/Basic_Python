# Argumentos parametros nombrados variables - keywords

print('======================')
print()

def mostrarIdentidad1(**identificacion):
    print(type(identificacion))
    print(identificacion)

mostrarIdentidad1()

print()

def mostrarIdentidad(**identificacion):
    resultado = ''

    if identificacion.get('documento'):
        resultado += 'Documento: ' + str(identificacion.get('documento')) + '\n'

    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'

    return resultado

persona = mostrarIdentidad(nombre = 'Mauricio', apellido = 'Posada')
print('Identificación:\n' + persona)

print()

persona = mostrarIdentidad(nombre = 'Mauricio', apellido = 'Posada', documento = 1983746)
print('Identificación:\n' + persona)

print('======================')