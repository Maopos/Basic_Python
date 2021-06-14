from functools import reduce
print('======================')
print()

print('=== Acumular ===')

listado = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def acumular(acumulador, elemento):
    return acumulador + elemento

resultado = reduce(acumular, listado)

print(resultado)

print('\n=== Ejemplo con reto 4 ===')


produccion = [[2001, ('Primera', 5, 5), ('Primera', 7, 5)], [2002, ('Segunda', 2, 5), ('Segunda', 4, 5)], [2003, ('Tercera', 7, 5), ('Tercera', 3, 5)]]

def extraer_fechas(listado):
    for i in listado:
        return i

numeros = list(map(extraer_fechas, produccion))


#-----------------------------

def iterar(listado):
    total_por_dia = []
    for i in listado:
        resultado_2 = list(filter(lambda x: type(x) == tuple, i))
        totales = [] 
        for i in resultado_2:
            resultado_3 = i[1] * i[2]
            if resultado_3 <= 30000000:
                resultado_3 += 50000
            totales.append(resultado_3)

            resultado_4 = reduce(lambda x=0, y=0: x + y, totales) 
        total_por_dia.append(resultado_4)
    return total_por_dia

suma_dia = iterar(produccion)

    
fecha_producc = list(zip(numeros, suma_dia))

print(fecha_producc)







        












print()
print('======================')