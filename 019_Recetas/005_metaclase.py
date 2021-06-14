print('======================')
print()

class NoInstanciar(type):

    def __call__(self, *args, **kwargs):

        raise TypeError('No se pueden crear objetos de esta clase')

class Constantes(metaclass = NoInstanciar):

    pi = 3.1416

    e = 2.7856

    eu = 0.577215



#c = Constantes() # -- Genera error


print(Constantes.pi)





print()
print('======================')