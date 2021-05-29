import sys
from typing import ValuesView

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demo QPushButton')
        self.setFixedSize(400, 400)

        self.btn_mostrar_mensaje = QPushButton('Mostrar mensaje', self)
        self.btn_mostrar_mensaje.setFixedWidth(150)
        self.btn_mostrar_mensaje.move(125, 150)
        self.btn_mostrar_mensaje.clicked.connect(self.mostrar_mensaje)

    def mostrar_mensaje(self):
        print('\nEl usuario ha presionado el boton para mostrar mensaje...\n')


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()