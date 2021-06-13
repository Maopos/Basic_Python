import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()

    def initGui(self):
        self.setWindowTitle('Selección de vuelo.')
        self.setFixedSize(500, 400)

        self.lbl_seleccion_vuelo = QLabel('Seleccione la clase de su vuelo:', self)
        self.lbl_seleccion_vuelo.move(50, 70)
        self.lbl_seleccion_vuelo.setFixedWidth(200)

        self.rbtn_1_clase = QRadioButton('Primera Clase.', self)
        self.rbtn_1_clase.move(50, 130)
        self.rbtn_1_clase.setFixedWidth(250)
        self.rbtn_1_clase.toggled.connect(self.seleccionar_clase)

        self.rbtn_2_clase = QRadioButton('Clase Negocios. ', self)
        self.rbtn_2_clase.move(50, 160)
        self.rbtn_2_clase.setFixedWidth(250)
        self.rbtn_2_clase.toggled.connect(self.seleccionar_clase)

        self.rbtn_3_clase = QRadioButton('Clase Económica.', self)
        self.rbtn_3_clase.move(50, 190)
        self.rbtn_3_clase.setFixedWidth(250)
        self.rbtn_3_clase.toggled.connect(self.seleccionar_clase)

        self.lbl_resultado_titulo = QLabel('Resultado:', self)
        self.lbl_resultado_titulo.move(50, 250)

        self.lbl_resultado = QLabel(self)
        self.lbl_resultado.move(50, 280)
        self.lbl_resultado.setFixedWidth(400)

    def seleccionar_clase(self):
        costo_vuelo = 0
        clase = ''
        

        if self.rbtn_1_clase.isChecked():
            costo_vuelo = '2.000.0'
            clase = 'Primera Clase'
        elif self.rbtn_2_clase.isChecked():
            costo_vuelo = '1.500.0'
            clase = 'Clase de Negocios'
        elif self.rbtn_3_clase.isChecked():
            costo_vuelo = '1.000.0'
            clase = 'Clase Económica'

        self.lbl_resultado.setText(f'El costo de su tiquete de {clase}, es de USD ${costo_vuelo}')


def main():
    app = QApplication(sys.argv)

    ventana = ventanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()