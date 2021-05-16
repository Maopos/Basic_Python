# Ejercicio 11.5: A través de una función validar si un número se halla en un rango.


print('======================')
print()

def buscar_numero(valor, rango):
    if isinstance(valor, (int, float)):
        if isinstance(rango, (list, tuple)):
            if len(rango) == 2:
                inicio = rango[0]
                final = rango[1]
                if inicio < final:
                    return valor in range(inicio, final + 1)
                else:
                    raise ValueError('EL primer valor debe ser menor al segundo valor.')
            else:
                raise Exception('El Rango debe tener 2 elementos.')
        else:
            raise TypeError('El Rango debe ser de tipo List o Tuple.')
    else:
        raise TypeError('El Valor debe ser de tipo int o float.')

numero = 1

rango_numeros = [0, 10]

try:
    resultado = buscar_numero(numero, rango_numeros)
    print(f'El valor {numero} se halla en el Rango {rango_numeros}: ', resultado)
except Exception as e:
    print('Error: ', e)



print()
print('======================')