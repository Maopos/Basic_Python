# Condiciones compuestas operador or

print()

tiempo_exp = int(input('Años de experiencia en programacion: '))
lenguaje = input('Lenguaje que domina: ')

if tiempo_exp >= 5 or lenguaje in ['Python', 'Java', 'Javascript']:
    print('Usted es apto para trabajar con nosotros.')
else:
    print('No es apto para trabajar co nosotros.')

print()