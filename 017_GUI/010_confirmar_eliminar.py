import sys
from PyQt6.QtGui import QIntValidator

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton, QLabel


class Ventanaprincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()

    def initGui(self):
        self.setWindowTitle('Eliminacion de producto por ID')
        self.setFixedSize(400, 400)

        self.lbl_producto = QLabel('Producto:', self)
        self.lbl_producto.move(60, 120)

        self.txt_producto = QLineEdit(self)
        self.txt_producto.move(140, 120)
        self.txt_producto.setFixedWidth(200)
        self.txt_producto.setValidator(QIntValidator())

        self.btn_eliminar = QPushButton('Eliminar', self)
        self.btn_eliminar.move(140, 170)
        self.btn_eliminar.setFixedWidth(200)
        self.btn_eliminar.clicked.connect(self.eliminar)

        self.lbl_resultado = QLabel('Resultado:', self)
        self.lbl_resultado.move(25, 250)

        self.lbl_resultado = QLabel(self)
        self.lbl_resultado.move(25, 270)
        self.lbl_resultado.setFixedWidth(350)
        #self.txt_resultado.setEnabled(False)
    
    def eliminar(self):
        confirmacion = QMessageBox(self)
        confirmacion.setText(f'Desea Eliminar el Producto con ID {self.txt_producto.text()}?')
        confirmacion.setIcon(QMessageBox.Icon.Question)
        confirmacion.setDetailedText('El producto se eliminará definitivamente...')
        confirmacion.setWindowTitle('Confirmación...')
        confirmacion.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        boton_yes = confirmacion.button(QMessageBox.StandardButton.Yes)

        confirmacion.exec()

        if confirmacion.clickedButton() == boton_yes:
            self.lbl_resultado.setText(f'Se ha eliminado el producto con ID {self.txt_producto.text()}.')
        else:
            self.lbl_resultado.setText(f'No se ha eliminado el producto con ID {self.txt_producto.text()}.')


        


def main():
    app = QApplication(sys.argv)

    ventana = Ventanaprincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()