from datetime import datetime
from collections import Counter

def registrar_producto(productos, producto):
    '''
    Registra un nuevo producto en el inventario.
    
    Parameters:
    productos: lista de productos en inventario
    producto: producto a agregar
    
    Returns:
    None
    '''
    productos.append(producto)

def realizar_venta(ventas, venta):
    '''
    Crea una nueva venta.
    
    Parameters:
    ventas: lista de las ventas realizadas
    venta: venta recien realizada
    
    Returns:
    None
    '''
    venta['fecha'] = datetime.now()
    ventas.append(venta)

def buscar_producto(productos, id_producto):
    '''
    Busca los datos de un producto por su id
    
    Parameters:
    productos: Listado de productos
    id_producto: id del producto a buscar               
    
    Returns:
    El producto encontrado
    None si no se encuentra
    '''
    for i in productos:
        if i['ID'] == id_producto:
            return i
    return None

def cambiar_estado_disponibildad(producto):
    '''
    Cambia el estado de disponibilidad de un producto
    
    Parameters:
    producto: producto a cambiar su disponibilidad
    
    Returns:
    None
    '''
    producto['Disponibilidad'] = not producto['Disponibilidad']

def generar_reporte_X_fecha(ventas, fecha_inicio, fecha_final):
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

    for i in ventas:
        if fecha_inicio <= i['fecha'] <= fecha_final:
            ventas_rango.append(i)

    return ventas_rango

def top_5_mas_vendidos(ventas):
    '''
    Muestra una lista con el top 5 de los productos mas vendidos.
    
    Parameters:
    ventas: listado de las ventas.
    
    Returns:
    lista de tuplas con el top 5 de los productos mas vendidos. (id_producto, cantidad)
    '''
    conteo_ventas = {}

    for i in ventas:
        if i['ID'] in conteo_ventas:
            conteo_ventas[i['ID']] += i['Cantidad']
        else:
            conteo_ventas[i['ID']] = i['Cantidad']
    
    conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

    contador = Counter(conteo_ventas)

    return contador.most_common(5)



def top_5_menos_vendidos(ventas):
    '''
    Muestra una lista con el top 5 de los productos menos vendidos.
    
    Parameters:
    ventas: listado de las ventas.
    
    Returns:
    lista de tuplas con el top 5 de los productos menos vendidos. (id_producto, cantidad)
    '''
    conteo_ventas = {}

    for i in ventas:
        if i['ID'] in conteo_ventas:
            conteo_ventas[i['ID']] += i['Cantidad']
        else:
            conteo_ventas[i['ID']] = i['Cantidad']
    
    conteo_ventas = {k: v for k, v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

    contador = Counter(conteo_ventas)

    return contador.most_common()[:-6:-1]

def mostrar_producto(producto):
    '''
    Muestra los datos de un producto.
    
    Parameters:
    producto: Producto a consultar
    
    Returns:
    None
    '''
    for i in producto:
        print('{}: {}'.format(i, producto[i]))
    
def mostrar_ventas(venta):
    '''
    Muestra los datos de una venta.
    
    Parameters:
    
    venta: Venta a consultar
    
    Returns:
    None
    '''
    for i in venta:
        print('{}: {}'.format(i, venta[i]))

def mostrar_datos_venta_producto(productos, datos_venta):
    producto = buscar_producto(productos, datos_venta[0])
    mostrar_producto(producto)
    print('Cantidad vendida: %i' % datos_venta[1])
    print()