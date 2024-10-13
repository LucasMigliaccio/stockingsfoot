import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtCore import QDir

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configurar la interfaz de usuario
        self.setWindowTitle('Seleccionar archivo Excel')
        self.setGeometry(300, 300, 400, 200)

        # Crear botón para abrir el diálogo
        self.layout = QVBoxLayout()
        self.button = QPushButton('Seleccionar archivo .xlsx', self)
        self.button.clicked.connect(self.open_file_dialog)
        
        # Añadir botón al layout
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def open_file_dialog(self):
        # Crear un QFileDialog para seleccionar archivos con la extensión .xlsx
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Seleccionar archivo Excel")
        file_dialog.setDirectory(QDir.homePath() + "/Desktop")  # Abre directamente en el escritorio
        file_dialog.setNameFilter("Archivos de Excel (*.xlsx)")
        
        if file_dialog.exec():
            # Obtener el nombre del archivo seleccionado
            selected_file = file_dialog.selectedFiles()[0]
            print(f"Archivo seleccionado: {selected_file}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    selector = FileSelector()
    selector.show()
    sys.exit(app.exec())
