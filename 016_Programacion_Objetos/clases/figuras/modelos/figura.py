from abc import ABC, abstractmethod

class Figura():
    def __init__(self, color, borde):
        self.color = color
        self.borde = borde
    
    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'Color: {self.color} - Borde: {self.borde}'