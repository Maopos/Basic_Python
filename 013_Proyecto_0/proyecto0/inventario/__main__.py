from .inventario_funciones import *
#import inventario_funciones as pro

import datetime


def mostrar_menu():
    '''
    Muestra menu de opciones.

    .
    '''
    print('\n===========================================================\n')
    print('Inventario\n')
    print('1 >>> Registro de nuevo Producto.')
    print('2 >>> Registro de nueva Venta.')
    print('3 >>> Búsqueda de un producto por código')
    print('4 >>> Cambiar disponibilidad de producto.')
    print('5 >>> Generar reporte productos vendidos en un rango de fecha.')
    print('6 >>> Ver top 5 de los productos más vendidos.')
    print('7 >>> Ver top 5 de los productos menos vendidos.')
    print()
    print('0 >>> Salir')
    print()

def capturar_entero(mensaje):
    '''
    Captura un numero entero con validacion
    
    Parameters:
    mensaje: Mensaje a mostrar
    
    Returns:
    Numero entero capturado
    '''
    while True:
        try:
            numero = int(input(f'{mensaje}: '))
            return numero
        except ValueError:
            print('\n*** Digite un numero entero. ***\n')
        
        print()

def capturar_float(mensaje):
    '''
    Captura un numero real con validacion
    
    Parameters:
    mensaje: Mensaje a mostrar
    
    Returns:
    Numero real capturado
    '''
    while True:
        try:
            numero = float(input(f'{mensaje}: '))
            return numero
        except ValueError:
            print('\n*** Digite un numero real. ***\n')
        
        print()

def capturar_string(mensaje):
    '''
    Captura un string con validacion
    
    Parameters:
    mensaje: Mensaje a mostrar
    
    Returns:
    String capturado
    '''
    while True:
        cadena = input(f'{mensaje}: ').strip() # strip() Eliminar espacios antes y despues del texto
        
        if len(cadena):
            return cadena
        else:
            print('\n*** No se ha digitado ningún texto aún. ***\n')

        print()

def listar_productos(productos):
    print(f'ID  Producto    Cantidad    Precio')
    for i in productos:
        print(f"{i['ID']}:      {i['Nombre']}       {i['Cantidad']}     {i['Precio']}")

def main():
    
    productos = []
    ventas = []

    while True:
        while True:
            try:
                mostrar_menu()
                opcion = int(input('Digite la operación a realizar: '))
                if 0 <= opcion <= 7:
                    break
                else:
                    print('\n*** Debe digitar un número positivo entre 0 y 7.!!! ***\n')
                
            except ValueError:
                print('\n*** Error: Digite una opcion válida. ***\n')

        if opcion == 0:
            break
        elif opcion == 1:
            print('\n-- Registro de nuevo Producto --\n')
            while True:
                id_producto = capturar_entero('Digite el ID del producto')
                producto = buscar_producto(productos, id_producto)

                if producto is None:
                    break
                else:
                    print('\n*** El ID digitado se encuentra en uso.!!! ***\n')

            nombre_producto = capturar_string('Digite el nombre del producto')

            while True:
                precio_producto = capturar_float('Digite el precio del producto')

                if precio_producto > 0:
                    break
                else:
                    print('\n*** Debe digitar un precio mayor a cero(0)!!! ***\n')

            while True:
                cantidad_producto = capturar_entero('Digite la cantidad de este producto')

                if cantidad_producto > 0:
                    break
                else:
                    print('\n*** Debe digitar una cantidad mayor a cero(0)!!! ***\n')
            
            while True:

                disponible = capturar_entero('Digite la disponibilidad, (1) = Disponible, (0) = No Disponible')

                if disponible == 1 or disponible == 0:
                    disponible = disponible == 1
                    break

            nuevo_producto = {'ID': id_producto, 'Nombre': nombre_producto,'Precio': precio_producto, 'Cantidad': cantidad_producto, 'Disponibilidad': disponible}

            registrar_producto(productos, nuevo_producto)

            print('\nEl nuevo producto se registro con éxito.\n')
            print(productos)
            
        elif opcion == 2:
            print('\n-- Registro de nueva Venta --\n')

            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a vender')
                    
                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')
                
                while True:
                    cantidad_producto = capturar_entero('Digite la cantidad a vender de este producto')

                    if cantidad_producto > 0 :
                        if cantidad_producto <= producto['Cantidad']:
                            break
                        else:
                            print(f"\n*** Debe digitar una cantidad menor o igual a {producto['Cantidad']} unidades de {producto['Nombre']}!!! ***\n")

                    else:
                        print('\n*** Debe digitar una cantidad mayor a cero(0)!!! ***\n')

                nueva_venta = {'ID': id_producto, 'Nombre': nombre_producto, 'Cantidad': cantidad_producto, 'Total sin Iva': producto['Precio'] * cantidad_producto}

                realizar_venta(ventas, nueva_venta)
                print('\nLa venta del producto se registro con éxito.\n')

            else:
                print('\n*** No existen productos para vender ***\n')


        elif opcion == 3:
            print('\n-- Buscar un producto por ID --\n')

            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a buscar')
                    print()
                    
                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')

                mostrar_producto(producto)

            else:
                print('\n*** No existen productos en el inventario. ***\n')

        elif opcion == 4:
            print('\n-- Cambiar disponibilidad de producto. --\n')

            if len(productos):
                while True:
                    listar_productos(productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a cambiar disponibilidad')
                    print()
                    
                    producto = buscar_producto(productos, id_producto)

                    if producto:
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')

                cambiar_estado_disponibildad(producto)
                mostrar_producto(producto)

            else:
                print('\n*** No existen productos en el inventario. ***\n')

        elif opcion == 5:
            print('\n-- Generar un reporte de ventas en un rango de fecha. --\n')

            if len(productos):
                if len(ventas):
                    while True:
                        try:
                            fecha_inicio = capturar_string('Digite la fecha de inicio (AAAA-MM-DD)')
                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break
                        except ValueError:
                            print('\n*** Digite correctamente la fecha (AAAA-MM-DD). ***\n')
                        print()

                    while True:
                        try:
                            fecha_final = capturar_string('Digite la fecha final (AAAA-MM-DD)')
                            fecha_final = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                            break
                        except ValueError:
                            print('\n*** Digite correctamente la fecha (AAAA-MM-DD). ***\n')
                        print()

                    ventas_rango = generar_reporte_X_fecha(ventas, fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for i in ventas_rango:
                            print()
                            mostrar_ventas(i)
                            print()
                    else:
                        print('\n*** No hay ventas registradas en ese rango de fecha. ***\n')
                
                else:
                    print('\n*** No hay ventas registradas. ***\n')

            else:
                print('\n*** No existen productos en el inventario. ***\n')

        elif opcion == 6:
            print('\n-- Top 5 productos mas vendidos. --\n')

            if len(productos):
                if len(ventas):
                    productos_mas_vendidos = top_5_mas_vendidos(ventas)

                    for i in productos_mas_vendidos:
                        mostrar_ventas(i)
                else:
                    print('\n*** No hay ventas registradas. ***\n')

            else:
                print('\n*** No existen productos en el inventario. ***\n')

        elif opcion == 7:
            print('\n-- Top 5 productos menos vendidos. --\n')

            if len(productos):
                if len(ventas):
                    productos_menos_vendidos = top_5_menos_vendidos(ventas)
                    
                    for i in productos_menos_vendidos:
                        mostrar_ventas(i)
                else:
                    print('\n*** No hay ventas registradas. ***\n')

            else:
                print('\n*** No existen productos en el inventario. ***\n')



    print('\n=== El programa ha finalizado. ==\n\n===========================================================\n')

if __name__ == '__main__':
    main()
