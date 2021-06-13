

class Carro:
    def __init__(self, nombre, placa, marca, modelo, pais):
        self.nombre = nombre
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.pais = pais
        self.estado = False

    def encender(self):
        if not self.estado:
            self.estado = True

    def apagar(self):
        if self.estado:
            self.estado = False

    def acelerar(self):
        if self.estado:
            print('El vehiculo ha acelerado.')

    def frenar(self):
        if self.estado:
            print('El vehiculo ha frenado')