import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demo QMessageBox')
        self.setFixedSize(400, 400)

        self.btn_mostrar_mensaje = QPushButton('Mostrar mensaje', self)
        self.btn_mostrar_mensaje.move(125, 150)
        self.btn_mostrar_mensaje.setFixedWidth(150)
        self.btn_mostrar_mensaje.clicked.connect(self.mostrar_mensaje)
    
    def mostrar_mensaje(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information) #Information, NoIcon, Question,Warning, Critical
        mensaje.setText('Ha hecho Click sobre el botón!!!')
        mensaje.setDetailedText('Hola..')
        mensaje.setWindowTitle('sdf')

        mensaje.exec()

def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()