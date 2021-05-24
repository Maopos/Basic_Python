# Creacion de objetos - instanciación
# Para importar crear archivo __init__.py en /modelos

from modelos.carro import Carro 

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




    
    
    print('\n======================')

if __name__ == '__main__':
    main()