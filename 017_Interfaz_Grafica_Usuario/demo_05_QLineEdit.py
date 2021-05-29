import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox, QLineEdit


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demo QLineEdit')
        self.setFixedSize(400, 400)
        

        self.txt_mensaje = QLineEdit(self)
        self.txt_mensaje.setFixedWidth(300)
        self.txt_mensaje.move(50, 150)

def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()