from .modelos.inventario import Inventario
from .modelos.producto import Producto
from .modelos.venta import Venta
import os
import pickle

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
    print('8 >>> Mostrar Inventario.')
    # print('9 >>> Guardar')
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
        print(f"{i.id_producto}      {i.nombre}       {i.cantidad}     {i.precio}")


def continuar():
    print('Presione Enter para continuar...', end='')
    input()

def cargar_inventario():
    with open('inventario/inventario.pickle', 'rb') as f:
        inventario = pickle.load(f)
        return inventario

def guardar_datos(inventario):
    with open('inventario/inventario.pickle', 'wb') as f:
        

        pickle.dump(inventario, f)



def main():

    inventario = Inventario()

    if os.path.isfile('inventario/inventario.pickle'):
        resultado = cargar_inventario()
        inventario.productos = resultado.productos
        inventario.ventas = resultado.ventas
        
    

    while True:
        while True:
            try:
                mostrar_menu()
                opcion = int(input('Digite la operación a realizar: '))
                if 0 <= opcion <= 8:
                    break
                else:
                    print('\n*** Debe digitar un número positivo entre 0 y 8 ***\n')
                
                continuar()
                
            except ValueError:
                print('\n*** Error: Digite una opcion válida. ***\n')

        if opcion == 0:
            break
        elif opcion == 1:
            print('\n-- Registro de nuevo Producto --\n')
            while True:
                id_producto = capturar_entero('Digite el ID del producto')

                if id_producto > 0:
                    
                    producto = inventario.buscar_producto(id_producto)
                
                    if producto is None:
                        break
                    else:
                        print('\n*** El ID digitado se encuentra en uso.!!! ***\n')
                else:
                    print('\n*** El ID debe ser mayor a cero (0) ***\n')
                

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

            nuevo_producto = Producto(id_producto, nombre_producto, precio_producto, cantidad_producto, disponible)

            inventario.registrar_producto(nuevo_producto)

            print('\nEl nuevo producto se registro con éxito.\n')
            listar_productos(inventario.productos)
            print()
            
        elif opcion == 2:
            print('\n-- Registro de nueva Venta --\n')

            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a vender')
                    
                    producto = inventario.buscar_producto(id_producto)

                    if producto:
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')
                
                while True:
                    cantidad_producto = capturar_entero('Digite la cantidad a vender de este producto')

                    if cantidad_producto > 0 :
                        if cantidad_producto <= producto.cantidad:
                            break
                        else:
                            print(f"\n*** Debe digitar una cantidad menor o igual a {producto.cantidad} unidades de {producto.nombre}!!! ***\n")

                    else:
                        print('\n*** Debe digitar una cantidad mayor a cero(0)!!! ***\n')
                
                

                nueva_venta = Venta(id_producto, producto.nombre, cantidad_producto, producto.precio * cantidad_producto)

                inventario.realizar_venta(nueva_venta)
                print('\nTotal venta: $%.2f' % (nueva_venta.total_sin_iva * 1.19))
                print('\nLa venta del producto se registro con éxito.\n')

            else:
                print('\n*** No existen productos para vender ***\n')


        elif opcion == 3:
            print('\n-- Buscar un producto por ID --\n')

            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a buscar')
                    print()
                    
                    producto = inventario.buscar_producto(id_producto)

                    if producto:
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')

                inventario.mostrar_producto(producto)
                print()

            else:
                print('\n*** No existen productos en el inventario. ***\n')

        elif opcion == 4:
            print('\n-- Cambiar disponibilidad de producto. --\n')

            if len(inventario.productos):
                while True:
                    listar_productos(inventario.productos)
                    id_producto = capturar_entero('\nDigite el ID del producto a cambiar disponibilidad')
                    print()
                    
                    producto = inventario.buscar_producto(id_producto)

                    if producto:
                        
                        break
                    else:
                        print('\n*** El ID no existe. ***\n')

                inventario.cambiar_estado_disponibildad(producto)
                inventario.mostrar_producto(producto)
                print()

            else:
                print('\n*** No existen productos en el inventario. ***\n')
            

        elif opcion == 5:
            print('\n-- Generar un reporte de ventas en un rango de fecha. --\n')

            if len(inventario.productos):
                if len(inventario.ventas):
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

                    ventas_rango = inventario.generar_reporte_X_fecha(fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for i in ventas_rango:
                            print()
                            inventario.mostrar_ventas(i)
                            print()
                    else:
                        print('\n*** No hay ventas registradas en ese rango de fecha. ***\n')
                    
                
                else:
                    print('\n*** No hay ventas registradas. ***\n')
                

            else:
                print('\n*** No existen productos en el inventario. ***\n')
            

        elif opcion == 6:
            print('\n-- Top 5 productos mas vendidos. --\n')

            if len(inventario.productos):
                if len(inventario.ventas):
                    productos_mas_vendidos = inventario.top_5_mas_vendidos()
                    

                    for i in productos_mas_vendidos:
                        inventario.mostrar_datos_venta_producto(i)
                        
                else:
                    print('\n*** No hay ventas registradas. ***\n')
                

            else:
                print('\n*** No existen productos en el inventario. ***\n')
            

        elif opcion == 7:
            print('\n-- Top 5 productos menos vendidos. --\n')

            if len(inventario.productos):
                if len(inventario.ventas):
                    productos_mas_vendidos = inventario.top_5_menos_vendidos()
                    

                    for i in productos_mas_vendidos:
                        inventario.mostrar_datos_venta_producto(i)
                        
                else:
                    print('\n*** No hay ventas registradas. ***\n')

            else:
                print('\n*** No existen productos en el inventario. ***\n')
        
        elif opcion == 8:
            print('\n-- Listado de productos. --\n')

            if len(inventario.productos):
                listar_productos(inventario.productos)
                
                print('\n-- Listado de ventas. --\n')

                for i in inventario.productos:
                    for k in inventario.ventas:
                        if i.id_producto == k.id_producto:
                            k.id_producto = i.id_producto
                    
                
                print(f'ID         Producto        Cantidad Vendida        Fecha')

                for i in inventario.ventas:
                    print(f"{i.id_producto}       {i.nombre}               {i.cantidad}                     {i.fecha}")



                print()
            else:
                print('\n*** No existen productos en el inventario. ***\n')
        
           
        continuar()
    
    if len(inventario.productos):
        if guardar_datos(inventario):
            print('\n** Se han guardado los datos con éxito.\n')
        else:
            ('No se han guardado los datos.')


    print('\n=== El programa ha finalizado. ==\n\n===========================================================\n')

if __name__ == '__main__':
    main()
