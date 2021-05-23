import pickle

print('======================')
print()

def main():
    
    print('=== Uso del modulo pikle para serilizar objetos en python. ===')
    
    capitales = {'Colombia': 'Bogotá', 'Perú': 'Lima', 'Ecuador': 'Quito', 'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia'}

    nombre_archivo = '014_Manipulacion_de_Archivos/capitales'

    with open(nombre_archivo, 'wb') as file:
        pickle.dump(capitales, file)


    
    
    print('=== Lectura del contenido de un archivo.pickle ===\n')
    
    with open(nombre_archivo, 'rb') as file:
        capitales_recuperado = pickle.load(file)

        print('Tipo de dato: ', type(capitales_recuperado))
        print('\nContenido: ', capitales_recuperado)
    
    
    print()
    print('\nEl programa ha terminado.\n')







if __name__ == '__main__':
    main()

print()
print('======================')