

class Clinica:

    def __init__(self, vacuna, pyp, odontologia, diabetes, ht, adulto_mayor):

        self.nombre = input('ingrese nombre paciente: ')
        self.apellido = input('ingrese apellido paciente:')
        self.edad = int(input('ingrese edad del paciente: '))

        self.adulto_mayor = adulto_mayor
        self.vacuna = vacuna
        self.pyp = pyp
        self.odontologia= odontologia
        self.diabetes = diabetes
        self.ht = ht
        
        
    def aplicar_vacunas(self):
        if self.edad >= 1: 
            print('Ud se debe aplicar 5 vacunas.')
        else:
            print('El paciente recibira otro tratamiento.')

    def verificar_adulto_mayor(self):
        if self.edad > 70:
            print('el paciente pasa a conuslta de control con medico')
        else:
            print('el paciente pasa a consulta de control con enfermera jefe')
        

    def verificar_pyp(self):
        if self.edad > 15:
            print('aplicar triple viral')
        else:
            print('aplicar tetanos')

    def verificar_odontologia(self):
        if self.edad < 8:
            print('se remite a higienen oral')
        else: 
            print('revision por odontologia')

    def verificar_diabetes(self):
        if self.diabetes == 'control mensual':
            print('debe estar encontrol mensual')
        else:
            print('debe rtecibir medicamentos')


paciente = Clinica('Polio', 'control mensual', 'higiene oral', 'control bimestral', 'control trimestral', 'control mensual')

paciente.aplicar_vacunas()
paciente.verificar_adulto_mayor()
paciente.verificar_pyp()
paciente.verificar_odontologia()
paciente.verificar_diabetes()