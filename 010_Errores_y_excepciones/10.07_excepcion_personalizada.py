# Creacion exepcion personalizada

print('======================')
print()

class ValorMinimoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ValorMinimoError: {}'.format(self.message)
        else:
            return 'Se ha generado el Error ValorMinimoError'

class ValorMaximoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ValorMaximoError: {}'.format(self.message)
        else:
            return 'Se ha generado el Error ValorMaximoError'

minimo = 10
maximo = 20

while True:
    try:
        numero = int(input('Escribe un numero entre {} y {}: '.format(minimo, maximo)))

        if numero < minimo:
            raise ValorMinimoError('Ha escrito un valor menor a {}'.format(minimo))
        elif numero > maximo:
            raise ValorMaximoError('Ha escrito un valor mayor a {}'.format(maximo))
        
        break

    except ValueError:
        print('** Debe escribir un numero entero valido.')
    except ValorMinimoError as e:
        print('Error: ', e)
    except ValorMaximoError as e:
        print('Error: ', e)
    print()

print('Tu numero es: ', numero)
print()
print('======================')