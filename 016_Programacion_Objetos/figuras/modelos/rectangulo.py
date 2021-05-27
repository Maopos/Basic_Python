from . figura import Figura

class Rectangulo(Figura):
    def __init__(self, color, borde, ancho, alto):
        super().__init__(color, borde)

        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        print(f'Se dibujo un Rectangulo de {self.ancho} de ancho y {self.alto} de alto.')

    def area(self):
        resultado = self.ancho * self.alto
        print('El area del Rectangulo es: ', resultado, 'mt2')

    def __str__(self):
        return f'{super().__str__()} - Ancho: {self.ancho} mts - Alto: {self.alto} mts'