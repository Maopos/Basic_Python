from . figura import Figura
import math


class Circulo(Figura):
    def __init__(self, color, borde, radio):
        super().__init__(color, borde)

        self.radio = radio
    

    def dibujar(self):
        print(f'Se dibujo un Circulo de {self.radio} de radio.')

    def area(self):
        resultado = math.pi * (self.radio**2)
        print('El area del Circulo es: ', resultado, 'mt2')

    def __str__(self):
        return f'{super().__str__()} - Radio: {self.radio} mts'