# Ejercicio 5.5: Remover los valores duplicados en una lista.

print()

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Venus', 'Mercurio', 'Venus', 'Tierra', 'Marte', 'Saturno', 'Neptuno', 'Urano']

print(planetas)
print('Cantidad de planetas: ', len(planetas))

print()

print('== Solucion 1 - convertir a set - convertir a list ==')
print()

planetas_unicos = set(planetas)

planetas2 = list(planetas_unicos)


print('== Se removieron duplicados ==')

print(planetas2)
print('Cantidad de planetas: ',len(planetas2))

print()

print('== Solucion 2 - ciclo for - not in - append ==')
print()

planetas_sin_repetir = []

for i in planetas:
    if i not in planetas_sin_repetir:
        planetas_sin_repetir.append(i)


print('== Se removieron duplicados ==')

print(planetas_sin_repetir)
print('Cantidad de planetas: ',len(planetas_sin_repetir))

print()