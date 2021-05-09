# Ejercicio 8.10. Validar si tres valores numéricos pueden pertenecer al esquema de colores RGB.

print()

red = int(input('Escriba el valor de Red: '))
green = int(input('Escriba el valor de Green: '))
blue = int(input('Escriba el valor de Blue: '))

if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
    print('Los valores %i para Red, %i para Green y %i para Blue, pertenecen al esquema de colores RGB.' %(red, green, blue))
else:
    print('Los valores %i para Red, %i para Green y %i para Blue, NO pertenecen al esquema de colores RGB.' %(red, green, blue))

print()