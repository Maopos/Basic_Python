from . empleado import Empleado

class Empleado_Horas(Empleado):
    def __init__(self, nombre, documento, correo, especialidad, horas, valor_hora):
        super().__init__(nombre, documento, correo, especialidad)

        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        total = super().calcular_salario() + self.horas * self.valor_hora
        return total