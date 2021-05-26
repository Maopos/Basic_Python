from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad, nombre_cientifico):
        self.nombre = nombre
        self.edad = edad
        self.nombre_cientifico = nombre_cientifico

    def comer(self):
        print('El animal esta comiendo.')
    def moverse(self):
        print('El animal se esta moviendo.')

    @abstractmethod
    def hablar(self):
        pass