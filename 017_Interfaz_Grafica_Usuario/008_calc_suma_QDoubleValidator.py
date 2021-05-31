import sys

from PyQt6.QtGui import QDoubleValidator

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLabel, QLineEdit

class Ventana_Calculadora(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Calculadora Suma 💻')
        self.setFixedSize(300, 400)

        self.lbl_numero_1 = QLabel('Número 1: ', self)
        self.lbl_numero_1.move(50, 50)

        self.lbl_numero_2 = QLabel('Número 2: ', self)
        self.lbl_numero_2.move(50, 100)

        self.txt_numero_1 = QLineEdit(self)
        self.txt_numero_1.setFixedWidth(100)
        self.txt_numero_1.move(150, 50)      
        self.txt_numero_1.setValidator(QDoubleValidator())

        self.txt_numero_2 = QLineEdit(self)
        self.txt_numero_2.setFixedWidth(100)
        self.txt_numero_2.move(150, 100)
        self.txt_numero_2.setValidator(QDoubleValidator())

        self.btn_sumar = QPushButton('Sumar', self)
        self.btn_sumar.setFixedWidth(100)
        self.btn_sumar.move(100, 170)
        self.btn_sumar.clicked.connect(self.sumar) # Evento Click
        
        self.lbl_resultado = QLabel('Resultado: ', self)
        self.lbl_resultado.move(50, 250)

        self.lbl_resultado = QLabel(self)
        self.lbl_resultado.setFixedWidth(100)
        self.lbl_resultado.move(150, 250)
        #self.lbl_resultado.setEnabled(False)
        

        

    def sumar(self):
        numero_1 = float(self.txt_numero_1.text())
        numero_2 = float(self.txt_numero_2.text())

        suma = numero_1 + numero_2
        self.lbl_resultado.setText(str(suma))


def main():
    app = QApplication(sys.argv)

    ventana = Ventana_Calculadora()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()