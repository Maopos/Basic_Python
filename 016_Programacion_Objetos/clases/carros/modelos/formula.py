from modelos.carro import Carro

class Formula_1(Carro):
    def __init__(self, nombre, placa, marca, modelo, pais, peso):
        super().__init__(nombre, placa, marca, modelo, pais)

        self.peso = peso

    def competir(self):
        print('El auto ingresa a la pista de carreras.')