# Creacion de archivo

print('======================')
print()

def main():
    
    nombre_archivo = '014_Manipulacion_de_Archivos/paises.txt'

    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write('Colombia')
        file.write('\n')
        file.write('Ecuador')
        file.write('\n')
        file.write('Argentina')
        file.write('\n')
        file.write('Perú')
        file.write('\n')
        file.write('Venezuela')
        file.write('\n')
        file.write('Bolivia')
        


if __name__ == '__main__':
    main()

print()
print('======================')

