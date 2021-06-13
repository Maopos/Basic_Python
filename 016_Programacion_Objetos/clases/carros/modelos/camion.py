from . carro import Carro

class Camion(Carro):
    def __init__(self, nombre, placa, marca, modelo, pais, carga):
        super().__init__(nombre, placa, marca, modelo, pais)

        self.carga = carga

    def cargar(self):
        print('La mercancia se esta cargando.')

    def descargar(self):
        print('La mercancia se esta descargando.')