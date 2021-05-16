# programa python con punto de entrada

print('======================')
print()

def saludar(mensaje):
    return mensaje

class persona:
    def __init__ (self, documento, nombre):
        self.documento = documento
        self.nombre = nombre


def main():
    mauricio = persona(9726604, 'Mauricio Posada')
    saludo = f' Hola, mi nombre es {mauricio.nombre}.'
    resultado = saludar(saludo)
    print(resultado) 

if __name__ == '__main__':
    main()

print(__name__)
print('======================')