from abc import ABC

class Empleado():
    SALARIO_BASE = 1000


    def __init__(self, nombre, documento, correo, especialidad):

        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.especialidad = especialidad

    def calcular_salario(self):
        total = self.SALARIO_BASE * 1.1
        return total

    def __str__(self):
        return f'Nombre: {self.nombre} - Documento: {self.documento} - Especialidad: {self.especialidad} - Correo: {self.correo}'

    