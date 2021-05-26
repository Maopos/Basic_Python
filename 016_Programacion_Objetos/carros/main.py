# Creacion de objetos - instanciación
# Para importar crear archivo __init__.py en /modelos

from modelos.carro import Carro 
from modelos.camion import Camion 
from modelos.deportivo import Deportivo
from modelos.volqueta import Volqueta
from modelos.formula import Formula_1

def main():
    print('======================\n')

    toreto = Carro('Toreto', 'ABC-123', 'Mazda', 2016, 'Mexico')
    
    print('Tipo de dato: ', type(toreto).__name__)
    print()

    print('=== Atributos ===')
    print()

    print('Nombre:  ', toreto.nombre)
    print()

    print('Placa:   ', toreto.placa)
    print('Marca:   ', toreto.marca)
    print('Modelo:  ', toreto.modelo)
    print('Pais:    ', toreto.pais)
    print('Estado:  ', 'Encendido' if toreto.estado else 'Apagado')

    print()
    
    print('=== Métodos ===\n')
    
    toreto.encender()
    print('Estado:  ', 'Encendido' if toreto.estado else 'Apagado')
    print()
    
    toreto.acelerar()
    toreto.frenar()
    print()

    toreto.apagar()
    print('Estado:  ', 'Encendido' if toreto.estado else 'Apagado')
    print()
    
    print('=== Instanciacion de un objeto Camion ===')
    
    ftr = Camion('FTR', 'SEK-234', 'Chevrolet', 2018, 'Colombia', '4 Tn')
    print()
    
    print('Nombre:      ', ftr.nombre)
    print()

    print('Placa:       ', ftr.placa)
    print('Marca:       ', ftr.marca)
    print('Modelo:      ', ftr.modelo)
    print('Pais:        ', ftr.pais)
    print('Cap. carga:  ', ftr.carga)
    print('Estado:      ', 'Encendido' if ftr.estado else 'Apagado')
    
    print()
    
    print('=== Metodos de Camion ===')
    print()

    ftr.cargar()
    ftr.descargar()
    print()

    ftr.encender()
    print('Estado:  ', 'Encendido' if ftr.estado else 'Apagado')
    print()
    
    ftr.acelerar()
    ftr.frenar()
    print()

    ftr.apagar()
    print('Estado:  ', 'Encendido' if ftr.estado else 'Apagado')
    print()

    print('=== Instanciacion de un objeto Deportivo ===')
    
    porsche = Deportivo('Porsche', 'ERT-658', 'Porsche 911', '2020', 'Italia', '24"', 'Super Deportivo')
    print()
    
    print('Nombre:      ', porsche.nombre)
    print()

    print('Placa:       ', porsche.placa)
    print('Marca:       ', porsche.marca)
    print('Modelo:      ', porsche.modelo)
    print('Pais:        ', porsche.pais)
    print('Rines:       ', porsche.rines)
    print('Tipo:        ', porsche.tipo)
    print('Estado:      ', 'Encendido' if porsche.estado else 'Apagado')
    
    print()
    
    print('=== Metodos de Deportivo ===')
    print()
    
    porsche.encender()
    print('Estado:  ', 'Encendido' if porsche.estado else 'Apagado')
    print()
    
    porsche.acelerar()
    porsche.frenar()
    print()

    porsche.apagar()
    print('Estado:  ', 'Encendido' if porsche.estado else 'Apagado')
    print()

    porsche.abrir_puertas()
    porsche.cerrar_puertas()


    print('=== Instanciacion de un objeto Volqueta ===')
    
    challenger = Volqueta('Challenger', 'FGT-298', 'Challenger', '2013', 'Brasil', '5 Tn', '$120.000/Tn')
    print()
    
    print('Nombre:      ', challenger.nombre)
    print()

    print('Placa:       ', challenger.placa)
    print('Marca:       ', challenger.marca)
    print('Modelo:      ', challenger.modelo)
    print('Pais:        ', challenger.pais)
    print('Cap. Carga:  ', challenger.carga_materiales)
    print('Costo:       ', challenger.costo_servicio)
    print('Estado:      ', 'Encendido' if challenger.estado else 'Apagado')
    
    print()
    
    print('=== Metodos de Volqueta ===')
    print()
    
    challenger.encender()
    print('Estado:  ', 'Encendido' if challenger.estado else 'Apagado')
    print()
    
    challenger.acelerar()
    challenger.frenar()
    print()

    challenger.apagar()
    print('Estado:  ', 'Encendido' if challenger.estado else 'Apagado')
    print()

    challenger.cargar_materiales()
    challenger.descargar_materiales()


    print('=== Instanciacion de un objeto Formula_1 ===')
    
    renault = Formula_1('Renault', 'TYU-850', 'Renault F11', 2009, 'Francia', '1,2 Tn')
    print()
    
    print('Nombre:      ', renault.nombre)
    print()

    print('Placa:       ', renault.placa)
    print('Marca:       ', renault.marca)
    print('Modelo:      ', renault.modelo)
    print('Pais:        ', renault.pais)
    print('Peso:        ', renault.peso)
    print('Estado:      ', 'Encendido' if renault.estado else 'Apagado')
    
    print()
    
    print('=== Metodos de Formula_1 ===')
    print()
    
    renault.encender()
    print('Estado:  ', 'Encendido' if renault.estado else 'Apagado')
    print()
    
    renault.acelerar()
    renault.competir()
    renault.frenar()
    print()

    renault.apagar()
    print('Estado:  ', 'Encendido' if renault.estado else 'Apagado')
    print()


    parque_automotor = [ftr, porsche, challenger, renault]

    
    
    print('=== Iteracion de todos los objetos. ===')
    
    
    
    print()

    for i in parque_automotor:
        print('Nombre:      ', i.nombre)
        print()

        print('Placa:       ', i.placa)
        print('Marca:       ', i.marca)
        print('Modelo:      ', i.modelo)
        print('Pais:        ', i.pais)
        print('Estado:      ', 'Encendido' if i.estado else 'Apagado')
        print()
        i.encender()
        i.acelerar()
        i.frenar()
        i.apagar()
        print('*********************************\n')


    print('\n======================')

if __name__ == '__main__':
    main()