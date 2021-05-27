from . figura import Figura


class Triangulo(Figura):
    def __init__(self, color, borde, base, altura):
        super().__init__(color, borde)

        self.base = base
        self.altura = altura

    def dibujar(self):
        print(f'Se dibujo un Triangulo de {self.altura} mts de altura y {self.base} mts de base.')

    def area(self):
        resultado = (self.base * self.altura) / 2
        print(f'El area del Triangulo es {resultado} mts2')

    def __str__(self):
        return f'{super().__str__()} - Base: {self.base} mts - Altura: {self.altura} mts'