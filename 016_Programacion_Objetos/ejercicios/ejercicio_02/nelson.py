class car:

    def __init__(self, añoFab, color, marca, pais, impuesto, precio):
        self.añoFab = añoFab
        self.color = color
        self.marca = marca
        self.pais = pais
        self.impuesto = impuesto
        self.precio = precio
        

    def año_de_fabrica(self):
        if self.añoFab > 2022:
            print('último modelo',self.añoFab)
        else:
            print('Modelo antiguo',self.añoFab)

    def caracteristicas(self):
        print(self.añoFab)
        print(self.color)
        print(self.marca)
        print(self.pais)
        

    def valor_real(self):
        valorTotal = self.precio + self.impuesto
        print('Valor total: ', valorTotal)

micarro = car(2001, 'negro', 'renault', 'colombia', 250000, 60000000)
valorTotal = 0

micarro.año_de_fabrica()
print()
micarro.caracteristicas()
print()
micarro.valor_real()