# Introduccion a la manipulacion de archivos de texto

def main():
    print('======================\n')

    print('=== Apertura de archivo de texto ===\n')

    nombre_archivo = '014_Manipulacion_de_Archivos/lenguajes.txt'

    # Abrir archivo
    archivo = open(nombre_archivo, 'r')

    # Operaciones en archivo
    for i in archivo.readlines():
        print(i, end='')
    
    # Cerrar archivo
    archivo.close()


    print()
    print()
    print('=== Apertura de archivo con manejador de contexto ===\n')

    nombre_archivo = '014_Manipulacion_de_Archivos/lenguajes.txt'

    with open(nombre_archivo, 'r') as f:
        for i in f.readlines():
            print(i, end='')

    print()

if __name__ == '__main__':
    main()

print('\n======================')