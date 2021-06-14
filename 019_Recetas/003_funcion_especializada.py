print('======================')
print()

def generador_multiplicador(num_1):
    return lambda x: x - num_1

duplicador = generador_multiplicador(2)

print(duplicador(3))
print(duplicador(4))
print(duplicador(5))

print()
print('======================')