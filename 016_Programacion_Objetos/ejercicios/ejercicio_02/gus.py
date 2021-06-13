class motor:

    def __init__(self, numero, cilindrage, combustible, velocidades, potencia):
        self.numero = numero
        self.cilindrage = cilindrage
        self.combustible = combustible
        self.velocidades = velocidades
        self.potencia = potencia

    def imprimir_numero_y_cilindraje(self):
        print(self.numero)
        print(self.cilindrage)

    def imprimir_combustible(self):
        print(self.combustible)

    def imprimir_velocidad_y_potencia(self):
        print(self.velocidades)
        print(self.potencia)



mymotor = motor('numero xy008978', 'cilinadrage 3000', 'combustible acpm', 'velocidades 6', 'potencia 3500')


mymotor.imprimir_combustible()
mymotor.imprimir_numero_y_cilindraje()
mymotor.imprimir_velocidad_y_potencia()