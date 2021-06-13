from modelos.empleado import Empleado
from modelos.empleado_comision import Empleado_Comision
from modelos.empleado_horas import Empleado_Horas
from modelos.empleado_nomina import Empleado_Nomina

def main():
    print('======================\n')
    
    empleados = []

    jorge = Empleado_Comision('Jorge Cardenas', '123456', 'jorge@mail.com', 'Ventas', 0.30, 10000)

    viviana = Empleado_Horas('Viviana Garcia', '345677', 'viviana@mail.com', 'Diseño Grafico', 80, 100)

    patricia = Empleado_Nomina('Patricia Toledo', '567889', 'patricia@mail.com', 'Finanazas', 0.10)

    empleados.append(jorge)
    empleados.append(viviana)
    empleados.append(patricia)

    for i in empleados:
        print(i)
        print(f'Salario: {i.calcular_salario()}')
        print()
    
    
    print('\n======================')

if __name__ == '__main__':
    main()