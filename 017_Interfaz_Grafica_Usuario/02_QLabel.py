import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demo Componente QLabel')
        self.setFixedSize(800, 600)

        self.lbl_message = QLabel('PyQt6 es genial!!!', self)
        self.lbl_message.move(10, 10)

def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()

    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()