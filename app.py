import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMessageBox
from database.database import get_connection, create_ventas_calzado_table, create_ventas_medias_table
from controllers.main_window import MainWindowForm


create_ventas_calzado_table()
create_ventas_medias_table()

if __name__ == "__main__":

    fecha_actual = datetime.now()

    if fecha_actual.month == 22 and fecha_actual.day == 15:
        # Crear una aplicación temporal para mostrar el mensaje
        app = QApplication()
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setWindowTitle("Advertencia")
        mensaje.setText("Su prueba gratuita ha concluido, Contacto: lucasmigliaccio10@gmail.com ")
        mensaje.exec()
        sys.exit()  # Salir del programa
        
    app = QApplication()
    window = MainWindowForm()
    window.show()

    sys.exit(app.exec())
