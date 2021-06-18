print('======================')
print()

def comprobarVocales():

    caracter = input('Escriba un caracter: ')
    
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        return f'El caracter {caracter} es vocal.'
    return f'El caracter {caracter} NO es vocal.'


print(comprobarVocales())

print()
print('======================')