import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QLineEdit


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Demo Ventana de Saludo!!!')
        self.setFixedSize(400, 400)

        self.lbl_nombre = QLabel('Nombre: ', self)
        self.lbl_nombre.move(75, 50)

        self.txt_nombre = QLineEdit(self)
        self.txt_nombre.setFixedWidth(250)
        self.txt_nombre.move(75, 80)

        self.btn_saludar = QPushButton('Saludar', self)
        self.btn_saludar.setFixedWidth(250)
        self.btn_saludar.move(75, 120)
        self.btn_saludar.clicked.connect(self.mostrar_saludo)

    def mostrar_saludo(self):
        nombre = self.txt_nombre.text().strip()

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Bienvenido!!!')

        if len(nombre):
            mensaje.setText(f'Hola, {nombre}!!!')
            mensaje.setIcon(QMessageBox.Icon.Information)
        else:
            mensaje.setText(f'No ha ingresado un nombre aún...')
            mensaje.setIcon(QMessageBox.Icon.Warning)
        
        mensaje.exec()



def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()