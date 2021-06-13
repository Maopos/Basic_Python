
class mascota:

    # definimos el metodo inicial(constructor)
    # self inicializa los atributos de la instancia que se esta inicializando
    def __init__(self, Tipo_mascota, raza, edad, sexo, vacunas, color):
        # atributo, propiedad, o caracteristica de la clase "Empleado"
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.Tipo_mascota = Tipo_mascota
        self.vacunas = vacunas
        self.color = color

    def Requierevacunas(self):  # comportamiento, funcionalidad, metodo
        if self.vacunas < 3:
            print('___Su Mascota Requiere vacunación!!!____')
        else:
            print('Su mascota se encuentra al dia con las vacunas')

    def rasgos(self):
        print("Su mascota es de color :", self.color)

    def claseMascota(self):
        print('Su mascota es un :', self.Tipo_mascota)


mypet = mascota('Gato', 'persa', '8 años', 'macho', 3, 'Cafe')
print('Su mascota es un: ', mypet.Tipo_mascota)
print('La cantidad de vacunas son: ', mypet.vacunas)
print('El sexo de su mascota es: ', mypet.sexo)
print('La edad es: ', mypet.edad)
print('El color de su mascota es:', mypet.color)

mypet.Requierevacunas()
mypet.rasgos()
mypet.claseMascota()
