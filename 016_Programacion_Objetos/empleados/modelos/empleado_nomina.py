from . empleado import Empleado

class Empleado_Nomina(Empleado):

    SALARIO = 2000

    def __init__(self, nombre, documento, correo, especialidad, porcentaje_prestaciones):
        super().__init__(nombre, documento, correo, especialidad)

        self.porcentaje_prestaciones = porcentaje_prestaciones
        

    
    def calcular_salario(self):
        total = super().calcular_salario() + self.SALARIO * (1 - self.porcentaje_prestaciones) 
        return total
