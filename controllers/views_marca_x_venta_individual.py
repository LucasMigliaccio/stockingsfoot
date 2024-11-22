import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.marcas_favoritas_individual import ViewMarcaIndividual
from database.queries_calzado import ventas_x_marca_individual

from models.producto import PandasModel


class ViewMarcaIndividualForm(QWidget, ViewMarcaIndividual):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.marcas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.productos_model = None  # Inicializar vacío
        self.init_table_model()
        

    def init_table_model(self):
        """Inicializa el modelo de datos y lo configura en la tabla."""
        try:
            # Llamar a la consulta sólo cuando se necesite
            data = ventas_x_marca_individual()
            df = pd.DataFrame(data)
            df.iloc[:, 2:] = df.iloc[:, 2:].abs()  # Asegurar que las columnas numéricas sean absolutas
            
            # Configurar el modelo PandasModel con los datos obtenidos
            self.marca_model = PandasModel(df)
            self.marcas_table.setModel(self.marca_model)
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            # Si falla, mostrar un modelo vacío o un mensaje
            self.marca_model = PandasModel(pd.DataFrame())
            self.marcas_table.setModel(self.marca_model)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    