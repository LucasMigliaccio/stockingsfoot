from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableView
from PySide6.QtCore import QAbstractTableModel, Qt
import pandas as pd
import sys

# Crear el DataFrame con tus datos, convirtiendo valores negativos a positivos
data = {
    "Grupo de ventas": [4414, 9187, 11780, 12398, 13319],
    "Zapatillas Mujer": [-2, -1, -4, -8, -4],
    "Botines Hombre": [-4, -1, -1, -3, -2],
    "Zapatillas Unisex": [-10, -5, -2, -9, -5],
    "Zapatillas Hombre": [-5, -5, -6, -8, -2],
    "Zapatillas Niña": [0, 0, -2, -2, 0],
    "Botines Unisex": [-2, -2, -3, 0, 0],
    "Zapatillas Niño": [-1, 0, 0, -3, 0],
    "Botines Niño": [-1, 0, 0, 0, 0]
}
df = pd.DataFrame(data)
df.iloc[:, 1:] = df.iloc[:, 1:].abs()  # Convertir valores a positivos

# Modelo de datos para integrar el DataFrame en QTableView
class PandasModel(QAbstractTableModel):
    def __init__(self, data_frame):
        super().__init__()
        self._data = data_frame

    def rowCount(self, index=None):
        return self._data.shape[0]

    def columnCount(self, index=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

class MainWindow(QMainWindow):
    def __init__(self, data_frame):
        super().__init__()
        self.setWindowTitle("Tabla de Ventas de Calzado")
        self.setGeometry(100, 100, 800, 400)

        # Configurar el widget central y el layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crear el QTableView y asociarlo con el modelo de pandas
        table_view = QTableView()
        model = PandasModel(data_frame)
        table_view.setModel(model)
        
        # Añadir el QTableView al layout
        layout.addWidget(table_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear la ventana principal y pasar el DataFrame
    main_window = MainWindow(df)
    main_window.show()

    sys.exit(app.exec())
