# programa python

print('======================')
print()

def saludar(mensaje):
    return mensaje

class persona:
    def __init__ (self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

mauricio = persona(9726604, 'Mauricio Posada')

saludo = f' Hola, mi nombre es {mauricio.nombre}.'

resultado = saludar(saludo)

print(resultado)

print()
print('======================')