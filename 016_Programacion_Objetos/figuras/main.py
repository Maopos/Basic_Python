from modelos.circulo import Circulo
from modelos.rectangulo import Rectangulo
from modelos.triangulo import Triangulo

def main():
    print('======================')
    print()

    figuras = []
    
    rectangulo_amarillo = Rectangulo('Amarillo', 'Negro', 10, 5)
    circulo_rojo = Circulo('Rojo', 'Negro', 5)
    triangulo_azul = Triangulo('Azul', 'Negro', 7, 10)

    figuras.append(rectangulo_amarillo)
    figuras.append(circulo_rojo)
    figuras.append(triangulo_azul)

    
    
    print('=== Area de las figuras ===\n')

    for i in figuras:
        i.dibujar()
        i.area()
        print()
        
    
    
    print()
    
    print('=== Sobreescritura de metodos. ===\n')
    
    print('Rectangulo: ', rectangulo_amarillo)
    print('Triangulo: ', triangulo_azul)
    print('Circulo: ', circulo_rojo)
    
    print()
    print('======================')

if __name__ == '__main__':
    main()