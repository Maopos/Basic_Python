print('======================')
print()


def cambiar_a_mayusculas(funcion):
    def envoltura():
        resultado = funcion()

        mayusculas = resultado.upper()

        return mayusculas

    return envoltura

@cambiar_a_mayusculas
def saludar():
    return 'Hola, Bienvenidos a Python'

print(saludar())

#----------------------------------------------

def dividir(funcion):
    def envoltura():
        resultado = funcion(5, 7)

        total = resultado / 2

        return total

    return envoltura


@dividir
def sumar(n, m):
    return n * m

print(sumar())

print()
print('======================')