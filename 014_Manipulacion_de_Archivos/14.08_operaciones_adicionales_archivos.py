import os

print('======================')
print()

def main():
    
    
    print('=== Operaciones adicionales sobre archivos ===\n')
    print('=== Renombrar archivos ===\n')

    nombre_archivo = '014_Manipulacion_de_Archivos/mi_nuevo_archivo.txt'
    
    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.\n')
    else:
        print(f'El archivo {nombre_archivo} NO existe en disco.\n')
    
    
    
    print()
    
    print('=== Renombrar ===\n')
    
    os.rename(nombre_archivo, '014_Manipulacion_de_Archivos/archivo.txt')

    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.\n')
    else:
        print(f'El archivo {nombre_archivo} NO existe en disco.\n')
    
    
if __name__ == '__main__':
    main()

print()
print('======================')