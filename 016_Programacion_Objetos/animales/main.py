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
    
    print('=== Nombres de Animales ===\n')
    
    for i in animales:
        print(i.nombre)
        
    print('\n=== Metodo hablar ===\n')
        
    for i in animales:
        i.hablar()   
        
    print()
    
    print('\n=== Atributos ===')
    print()

    

    
    
    print('\n======================')

if __name__ == '__main__':
    main()