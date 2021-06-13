from modelos.carro import Carro

class Volqueta(Carro):
    def __init__(self, nombre, placa, marca, modelo, pais, carga_materiales, costo_servicio):
        super().__init__(nombre, placa, marca, modelo, pais)

        self.carga_materiales = carga_materiales
        self.costo_servicio = costo_servicio

    def cargar_materiales(self):
        print('Los materiales se estan cargando.')

    def descargar_materiales(self):
        print('Los materiales se estan descargando.')