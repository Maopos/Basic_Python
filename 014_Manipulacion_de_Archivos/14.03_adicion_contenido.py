def main():

    print('=== Adicionar contenido a un archivo de texto ===')
   
    nombre_archivo = '014_Manipulacion_de_Archivos/paises.txt'

    with open(nombre_archivo, 'a+', encoding='utf-8') as file:
        file.write('\n')
        file.write('Brasil')
        file.write('\n')
        file.write('Uruguay')
        file.write('\n')
        file.write('Paraguay')
        file.write('\n')
        file.write('Chile')
       
    print('El programa ha finalizado.')

if __name__ == '__main__':
    main()

