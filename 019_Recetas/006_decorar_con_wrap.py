print('======================')
print()

from functools import wraps

def funcion_decoradora(funcion):

    @wraps(funcion)
    def envoltura(*args, **kwds):
        print('funcion decoradora invocada')

        return funcion(*args, **kwds)
    
    return envoltura


@funcion_decoradora
def saludar():
    print('Hola')



saludar()


print()
print('======================')