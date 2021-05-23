def main():
   
   
    print('===  Creacion de un archivo binario ===')
   
    nombre_archivo = '014_Manipulacion_de_Archivos/numeros.bin'

    archivo = open(nombre_archivo, 'wb')

    numeros = [2, 3, 5, 7, 11]

    archivo.write(bytearray(numeros))

    archivo.close()
   
    print()

if __name__ == '__main__':
    main()

    