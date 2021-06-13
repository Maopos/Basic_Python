import sys

from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()

    def initGui(self):
        self.setWindowTitle('Mi Aplicación.')
        self.setFixedSize(600, 600)

        # Pestañas
        self.mbr_principal = self.menuBar()
        self.menu_archivo = self.mbr_principal.addMenu('Archivo')
        self.menu_operaciones = self.mbr_principal.addMenu('Operaciones')
        self.menu_ayuda = self.mbr_principal.addMenu('Ayuda')

        # Archivo
        self.mni_salir = QAction('Salir', self)
        self.mni_salir.setShortcut('⌘D')           
        self.mni_salir.setStatusTip('Salir de la Aplicación')
        self.mni_salir.triggered.connect(self.close)
        
        self.menu_archivo.addAction(self.mni_salir)

        # Operaciones
        self.mni_copiar = QAction('Copiar 📑', self)
        self.mni_copiar.setShortcut('⌘C')                   
        self.menu_operaciones.addAction(self.mni_copiar)

        self.mni_cortar = QAction('Cortar ✂️', self)
        self.mni_cortar.setShortcut('⌘X') 
        self.menu_operaciones.addAction(self.mni_cortar)

        self.mni_pegar = QAction('Pegar 📥', self)
        self.mni_pegar.setShortcut('⌘V')                  
        self.menu_operaciones.addAction(self.mni_pegar)
        

        # Ayuda
        self.mni_acerca_de = QAction('A cerca de')
        self.menu_ayuda.addAction(self.mni_acerca_de)
        self.mni_acerca_de.triggered.connect(self.mostrar_acerca_de)

    def mostrar_acerca_de(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Acerca de')
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setText('A cerca de Mi Aplicación.\n\nAplicacion PyQt6.\nDesarrollador: Mauricio Posada.\nVersion 1.0.0\n2021.')

        mensaje.exec()



def main():
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()