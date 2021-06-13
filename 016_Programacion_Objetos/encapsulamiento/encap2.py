print('======================\n')

class Persona:

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo  # Publico
        self._nombre = nombre # Protegido solo acceden su clase y subclases
        self.__edad = edad # Privado solo accede su clase

    def __saludar(self):
        print('Hola', self.nombre)

pers_1 = Persona(1001, 'Mauricio Posada', 41)

print(pers_1.codigo)
print(pers_1._nombre)
print(pers_1._Persona__edad)

print()

pers_1.nombre = 'Jennifer Sepulveda'
pers_1._Persona__saludar()

print()

pers_1._Persona__edad = 34
print(pers_1._Persona__edad)


print('\n======================')