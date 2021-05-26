from modelos.carro import Carro

class Deportivo(Carro):
    def __init__(self, nombre, placa, marca, modelo, pais, rines, tipo):
        super().__init__(nombre, placa, marca, modelo, pais)

        self.rines = rines
        self.tipo = tipo

    def abrir_puertas(self):
        print('Las puertas se estan abriendo.')

    def cerrar_puertas(self):
        print('Las puertas se estan cerrando.')
    