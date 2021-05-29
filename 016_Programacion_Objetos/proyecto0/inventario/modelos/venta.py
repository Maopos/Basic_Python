from datetime import datetime

class Venta:
    def __init__(self, id_producto, nombre, cantidad, total_sin_iva):
        self.id_producto = id_producto
        self.nombre = nombre
        self.fecha = datetime.now()
        self.cantidad = cantidad
        self.total_sin_iva = total_sin_iva
