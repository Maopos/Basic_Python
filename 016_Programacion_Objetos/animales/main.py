from modelos.pato import Pato
from modelos.gato import Gato
from modelos.perro import Perro



def main():
    print('======================\n')

    animales = []

    donald = Pato('Donald', '2 años', 'Anas Platyrhychos domesticus', 'Verde')
    felix = Gato('Felix', '1 año', 'Felis catus', True)
    pluto = Perro('Pluto', '3 años', 'Canis lupus familiares', 'Terrier')

    animales.append(donald)
    animales.append(felix)
    animales.append(pluto)
    
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