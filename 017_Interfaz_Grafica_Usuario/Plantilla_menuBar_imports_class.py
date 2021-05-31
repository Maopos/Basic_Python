import sys

from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QInputDialog, QPushButton

class Captura_Datos(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()

    def initGui(self):
        self.setWindowTitle('My Application!!!')
        self.setFixedSize(600, 400)
        #self.showFullScreen()

        # Label
        self.lbl_saludo = QLabel('Bienvenido...', self)
        self.lbl_saludo.move(50, 50)
        

        # Menu 
        self.menu_principal = self.menuBar()
        self.menu_archivo = self.menu_principal.addMenu('Archivo')
        self.menu_operaciones = self.menu_principal.addMenu('Operaciones')
        self.menu_ayuda = self.menu_principal.addMenu('Ayuda')

        # Archivo
        self.menu_item_salir = QAction('Salir', self)
        self.menu_item_salir.setShortcut('⌘D')
        self.menu_item_salir.triggered.connect(self.close)
        self.menu_archivo.addAction(self.menu_item_salir)

        # Operaciones
        self.menu_item_operaciones = QAction('Operaciones', self)
        self.menu_operaciones.addAction(self.menu_item_operaciones)

        # Ayuda
        self.menu_acerca_de = QAction('Acerca de MY Application.', self)
        self.menu_ayuda.addAction(self.menu_acerca_de)
        self.menu_ayuda.triggered.connect(self.mostrar_acerca_de)

    def mostrar_acerca_de(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setText('A cerca de My Application.\n\nPyQt6 App.\nDesarrollador: Mauricio Posada.\nVersión: 1.0.0\n2021.')

        mensaje.exec()

def main():
    app = QApplication(sys.argv)

    ventana = Captura_Datos()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()