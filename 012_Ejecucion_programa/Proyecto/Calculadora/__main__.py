from .funciones_aritmeticas import sumar, restar, multiplicar, dividir

def menu():
    print('\n====================================\n')
    print('==== Calculadora: ====\n')
    print('Sumar:          1')
    print('Restar:         2')
    print('Multiplicar:    3')
    print('Dividir:        4')
    print()
    print('Salir:          0')
    print()

def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input('Digite la operación a realizar: '))
                break
            except TypeError as e:
                print('Error: Valor inválido')
        print()

        if opcion == 0:
            break

        if 1 <= opcion <= 4:
            while True:
                try:
                    num_1 = int(input('Digite el primer número: '))
                    break
                except ValueError as e:
                    print('Error: Valor inválido')
            while True:
                try:
                    num_2 = int(input('Digite el segundo número: '))
                    break
                except ValueError as e:
                    print('Error: Valor inválido')
                
        if opcion == 1:
            resultado = sumar(num_1, num_2)
            print(f'\n** Resultado: {num_1} + {num_2} = ', resultado)
        elif opcion == 2:
            resultado = restar(num_1, num_2)
            print(f'\n** Resultado: {num_1} - {num_2} = ', resultado)
        elif opcion == 3:
            resultado = multiplicar(num_1, num_2)
            print(f'\n** Resultado: {num_1} * {num_2} = ', resultado)
        elif opcion == 4:
            try:
                resultado = dividir(num_1, num_2)
                print(f'\n** Resultado: {num_1} / {num_2} = ', resultado)
            except ZeroDivisionError as e:
                print(e)
    print()

    print('El programa ha terminado.\n\n====================================\n')

if __name__ == '__main__':
    main()
    