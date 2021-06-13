import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Hola PyQt6')
        self.setFixedSize(500, 400)


def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()

    