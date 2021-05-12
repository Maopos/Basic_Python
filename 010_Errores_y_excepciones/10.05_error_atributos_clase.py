# Error al intentar acceder a un atributo inexistante en una clase

print('======================')
print()

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio


computador = Producto('001', 'Apple MacBook Air M1', 1000)


try:
    print('Codigo: ', computador.id)
    print('Nombre: ', computador.nombre)
    print('Precio: ', computador.precio)
    print('Precio: ', computador.cantidad)
except AttributeError as e:
    print('Atributo no existente.')
    print('Error: ', e)

print()
print('======================')