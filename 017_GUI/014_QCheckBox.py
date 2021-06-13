import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QInputDialog


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()
    
    def initGui(self):
        self.setWindowTitle('Pizza & Ingredientes.')
        self.setFixedSize(400, 450)

        self.lbl_precio_base = QLabel('Precio base Pizza: $15', self)
        self.lbl_precio_base.move(50, 50)
        self.lbl_precio_base.setFixedWidth(300)

        self.lbl_adicionales = QLabel('Ingredientes Adicionales.', self)
        self.lbl_adicionales.move(80, 100)
        self.lbl_adicionales.setFixedWidth(300)

        self.cbx_1 = QCheckBox('Queso Mozzarela.    $1', self)
        self.cbx_1.move(80, 130)
        self.cbx_1.setFixedWidth(250)
        self.cbx_1.stateChanged.connect(self.calcular_total)

        self.cbx_2 = QCheckBox('Pepperoni.                $2', self)
        self.cbx_2.move(80, 160)
        self.cbx_2.setFixedWidth(250)
        self.cbx_2.stateChanged.connect(self.calcular_total)

        self.cbx_3 = QCheckBox('Tocineta.                   $3', self)
        self.cbx_3.move(80, 190)
        self.cbx_3.setFixedWidth(250)
        self.cbx_3.stateChanged.connect(self.calcular_total)

        self.lbl_total = QLabel('Valor del pedido:', self)
        self.lbl_total.move(50, 250)
        self.lbl_total.setFixedWidth(300)

        self.lbl_resultado = QLabel(self)
        self.lbl_resultado.move(50, 280)
        self.lbl_resultado.setFixedSize(300, 100)

    def calcular_total(self):
        pizza = 15
        adicion = 0

        if self.cbx_1.isChecked():
            adicion += 1
        if self.cbx_2.isChecked():
            adicion += 2
        if self.cbx_3.isChecked():
            adicion += 3
                


        

       

        total = float(adicion + pizza) 

        self.lbl_resultado.setText(f'Pizza:             USD ${float(pizza)}\nAdicionales:  USD ${float(adicion)}\n\nEl Precio Total de la Pizza es de USD ${total}')
        


def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()