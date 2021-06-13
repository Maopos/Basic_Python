print('======================\n')

class Cliente:

    def __init__(self):

        self.__codigo = 4321

    def __cuenta(self):
        print('Cuenta de procesamiento')
    
    def getcodigo(self):
        return self.__codigo
    
persona = Cliente()  

# metodo get
print(persona.getcodigo())

# objeto._nombreclase atributo
print(persona._Cliente__codigo)

# metodo protegido
persona._Cliente__cuenta()




print('\n======================')