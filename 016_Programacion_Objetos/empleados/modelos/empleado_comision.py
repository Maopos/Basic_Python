from . empleado import Empleado

class Empleado_Comision(Empleado):
    def __init__(self, nombre, documento, correo, especialidad, porcentaje_comision, monto):
        super().__init__(nombre, documento, correo, especialidad)

        self.porcentaje_comision = porcentaje_comision
        self.monto = monto

    def calcular_salario(self):
        total = super().calcular_salario() + self.monto * self.porcentaje_comision
        return total