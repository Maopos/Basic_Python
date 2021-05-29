from collections import Counter
from .producto import Producto
from .venta import Venta

class Inventario:
    def __init__(self):
        self.productos = []
        self.ventas = []

     

    def registrar_producto(self, producto):
        '''
        Registra un nuevo producto en el inventario.
        
        Parameters:
        productos: lista de productos en inventario
        producto: producto a agregar
        
        Returns:
        None
        '''
        self.productos.append(producto)

    def realizar_venta(self, venta):
        '''
        Crea una nueva venta.
        
        Parameters:
        ventas: lista de las ventas realizadas
        venta: venta recien realizada
        
        Returns:
        None
        '''
        self.ventas.append(venta)

    def buscar_producto(self, id_producto):
        '''
        Busca los datos de un producto por su id
        
        Parameters:
        productos: Listado de productos
        id_producto: id del producto a buscar               
        
        Returns:
        El producto encontrado
        None si no se encuentra
        '''
        for i in self.productos:
            if i.id_producto == id_producto:
                return i
        return None

    def cambiar_estado_disponibildad(self, producto):
        '''
        Cambia el estado de disponibilidad de un producto
        
        Parameters:
        producto: producto a cambiar su disponibilidad
        
        Returns:
        None
        '''
        producto.disponibilidad = not producto.disponibilidad

    def generar_reporte_X_fecha(self, fecha_inicio, fecha_final):
        '''
        Genera un reporte de las ventas realizadas en un rango de fechas
        
        Parameters:
        ventas: lista de las ventas realizadas
        fecha_inicio: fecha inicial
        fecha_final: fecha final
        
        Returns:
        Listado de ventas realizadas en el rango especificado
        '''
        ventas_rango = []

        for i in self.ventas:
            if fecha_inicio <= i.fecha <= fecha_final:
                ventas_rango.append(i)

        return ventas_rango

    def top_5_mas_vendidos(self):
        '''
        Muestra una lista con el top 5 de los productos mas vendidos.
        
        Parameters:
        ventas: listado de las ventas.
        
        Returns:
        lista de tuplas con el top 5 de los productos mas vendidos. (id_producto, cantidad)
        '''
        conteo_ventas = {}

        for i in self.ventas:
            if i.id_producto in conteo_ventas:
                conteo_ventas[i.id_producto] += i.cantidad
            else:
                conteo_ventas[i.id_producto] = i.cantidad
        
        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

        contador = Counter(conteo_ventas)

        return contador.most_common(5)



    def top_5_menos_vendidos(self):
        '''
        Muestra una lista con el top 5 de los productos menos vendidos.
        
        Parameters:
        ventas: listado de las ventas.
        
        Returns:
        lista de tuplas con el top 5 de los productos menos vendidos. (id_producto, cantidad)
        '''
        conteo_ventas = {}

        for i in self.ventas:
            if i.id_producto in conteo_ventas:
                conteo_ventas[i.id_producto] += i.cantidad
            else:
                conteo_ventas[i.id_producto] = i.cantidad
        
        conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

        contador = Counter(conteo_ventas)

        return contador.most_common()[:-6:-1]

    def mostrar_producto(self, producto):
        '''
        Muestra los datos de un producto.
        
        Parameters:
        producto: Producto a consultar
    
        Returns:
        None
        '''
        for i in self.productos:
            print('ID: {}\nNombre: {}\nCantidad: {}\nPrecio: {}\nDisponibilidad: {}'.format(i.id_producto, i.nombre, i.cantidad, i.precio, i.disponibilidad))
        
    def mostrar_ventas(self, venta):
        '''
        Muestra los datos de una venta.
        
        Parameters:
        
        venta: Venta a consultar
        
        Returns:
        None
        '''
        print('ID: {}\nNombre: {}\nCantidad vendida: {}\nFecha: {}'.format(venta.id_producto, venta.nombre, venta.cantidad, venta.fecha))

    def mostrar_datos_venta_producto(self, datos_venta):
        producto = self.buscar_producto(datos_venta[0])
        self.mostrar_producto(producto)
        print('Cantidad vendida: %i' % datos_venta[1])
        print()   