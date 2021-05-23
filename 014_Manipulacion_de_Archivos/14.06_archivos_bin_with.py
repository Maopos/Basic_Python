print('======================')
print()

def main():
    
    nombre_archivo = '014_Manipulacion_de_Archivos/numeros.bin'

    print('Se está creando una archivo binario.\n')

    with open(nombre_archivo, 'wb') as file:

        numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 100]

        file.write(bytearray(numeros))

    #----------------------------------------------------------

    print('\nEste es el contenido del archivo "numeros.bin"\n')

    with open(nombre_archivo, 'rb') as file:

       numeros = list(file.read())

       print(numeros)

    print('\nEl programa finalizó correctamente.')


if __name__ == '__main__':
    main()

print()
print('======================')