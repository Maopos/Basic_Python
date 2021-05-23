print('======================')
print()

def main():

   
    print('=== Lectura de Archivo binario ===')
   
    nombre_archivo = '014_Manipulacion_de_Archivos/numeros.bin'

    archivo = open(nombre_archivo, 'rb')

    numeros = list(archivo.read())

    archivo.close()

    print()
    print(numeros)
    print()
   
    print('El programa finalizó')

if __name__ == '__main__':
    main()

print()
print('======================')