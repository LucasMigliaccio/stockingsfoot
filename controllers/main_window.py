import os
import PySide6.QtGui
from PySide6.QtWidgets import QWidget, QFileDialog, QVBoxLayout

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi

class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.init_ui() 

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def init_ui(self):
        # Configuramos el layout
        layout = QVBoxLayout()

        # Creamos el botón
        self.medias_pushButton.clicked.connect(self.abrir_medias_archivos)
        self.pushButton.clicked.connect(self.abrir_calzados_archivos)

        # Añadimos el botón al layout
        #layout.addWidget(self.medias_pushButton)


        # Configuramos la ventana principal
        self.setLayout(layout)
        self.setWindowTitle("Ejemplo QFileDialog")

    def abrir_medias_archivos(self):
        # Abrimos un QFileDialog cuando se presiona el botón
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*)")
        if archivo:
            print(f"Archivo seleccionado MEDIAS: {archivo}")

    def abrir_calzados_archivos(self):
        # Abrimos un QFileDialog cuando se presiona el botón
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*)")
        if archivo:
            print(f"Archivo seleccionado CALZADOS : {archivo}")