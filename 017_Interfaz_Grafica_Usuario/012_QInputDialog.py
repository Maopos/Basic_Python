import sys

from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QInputDialog, QPushButton

class Captura_Datos(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initGui()

    def initGui(self):
        self.setWindowTitle('Aplicación Captura de Datos')
        self.setFixedSize(400, 400)
        #self.showFullScreen()

        # Botones
        self.btn_nombre = QPushButton('Nombre Completo', self)
        self.btn_nombre.setFixedWidth(200)
        self.btn_nombre.move(100, 30)
        self.btn_nombre.clicked.connect(self.capturar_nombre)

        self.btn_edad = QPushButton('Edad', self)
        self.btn_edad.setFixedWidth(200)
        self.btn_edad.move(100, 60)
        self.btn_nombre.clicked.connect(self.capturar_edad)

        self.btn_ahorros = QPushButton('Ahorros', self)
        self.btn_ahorros.setFixedWidth(200)
        self.btn_ahorros.move(100, 90)
        self.btn_nombre.clicked.connect(self.capturar_ahorros)

        self.btn_color = QPushButton('Color', self)
        self.btn_color.setFixedWidth(200)
        self.btn_color.move(100, 120)
        self.btn_nombre.clicked.connect(self.capturar_color)

        # Resultado
        self.lbl_resultado = QLabel('Información personal:', self)
        self.lbl_resultado.move(100, 180)
        self.lbl_resultado.setFixedWidth(200)

        # Etiquetas de datos
        self.lbl_nombre = QLabel('Nombre Completo:', self)
        self.lbl_nombre.move(50, 240)
        self.lbl_nombre.setFixedWidth(200)

        self.lbl_nombre = QLabel('Edad:', self)
        self.lbl_nombre.move(50, 270)
        self.lbl_nombre.setFixedWidth(200)

        self.lbl_nombre = QLabel('Ahorros:', self)
        self.lbl_nombre.move(50, 300)
        self.lbl_nombre.setFixedWidth(200)

        self.lbl_nombre = QLabel('Color:', self)
        self.lbl_nombre.move(50, 330)
        self.lbl_nombre.setFixedWidth(200)

        # Etiquetas de resultados
        self.lbl_nombre_result = QLabel(self)
        self.lbl_nombre_result.move(200, 240)
        self.lbl_nombre_result.setFixedWidth(200)

        self.lbl_edad_result = QLabel(self)
        self.lbl_edad_result.move(200, 270)
        self.lbl_edad_result.setFixedWidth(200)

        self.lbl_ahorros_result = QLabel(self)
        self.lbl_ahorros_result.move(200, 300)
        self.lbl_ahorros_result.setFixedWidth(200)

        self.lbl_color_result = QLabel(self)
        self.lbl_color_result.move(200, 330)
        self.lbl_color_result.setFixedWidth(200)

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
        self.menu_acerca_de = QAction('Acerca de Aplicación Captura de Datos.', self)
        self.menu_ayuda.addAction(self.menu_acerca_de)
        self.menu_ayuda.triggered.connect(self.mostrar_acerca_de)

    def mostrar_acerca_de(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setText('A cerca de Aplicación captura de datos.\n\nAplicacion PyQt6.\nDesarrollador: Mauricio Posada.\nVersión: 1.0.0\n2021.')

        mensaje.exec()

    def capturar_nombre(self):
        nombre, ok = QInputDialog.getText(self,'Captura de datos.', 'Escribe tu nombre completo:')

        if ok:
            nombre = nombre.strip()

            if len(nombre):
                self.lbl_nombre_result.setText(nombre)

    def capturar_edad(self):
        edad, ok = QInputDialog.getInt(self,'Captura de datos.', 'Escribe tu edad:', 10, 1, 80)

        if ok:
            self.lbl_edad_result.setText(str(edad))

    def capturar_ahorros(self):
        ahorros, ok = QInputDialog.getDouble(self,'Captura de datos.', 'Escribe tu cantidad de ahorros:', 0, 1000, 1000000) # Minimo, incremento, Maximo

        if ok:
            self.lbl_ahorros_result.setText(str(ahorros))

    def capturar_color(self):
        colores =['Amarillo', 'Azul','Blanco', 'Rojo', 'Verde', 'Negro', 'Morado']

        color, ok = QInputDialog.getItem(self, 'Captura de datos.', 'Selecciona un color.', colores, 0, False) # 0 inicia desde el color[0], False no permite editar la lista de colores

        if ok:
            self.lbl_color_result.setText(color)

def main():
    app = QApplication(sys.argv)

    ventana = Captura_Datos()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()