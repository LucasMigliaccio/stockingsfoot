import os
import pandas as pd
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.ventas_x_categoria_individual import ViewProductos

from database.queries_calzado import ventas_x_categoria_individual, ventas_x_categoria_grupal

from models.producto import PandasModel


class ViewCategoriasForm(QWidget, ViewProductos):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.productos_table.setSelectionBehavior(QAbstractItemView.SelectRows) 

        # Configurar modelo de datos y tabla
        self.productos_model = None  # Inicializar vacío
        self.init_table_model()

        # Calcular y mostrar el total
        self.total_calzados()

    def init_table_model(self):
        """Inicializa el modelo de datos y lo configura en la tabla."""
        try:
            # Llamar a la consulta sólo cuando se necesite
            data = ventas_x_categoria_individual()
            df = pd.DataFrame(data)
            df.iloc[:, 1:] = df.iloc[:, 1:].abs()  # Asegurar que las columnas numéricas sean absolutas
            
            # Configurar el modelo PandasModel con los datos obtenidos
            self.productos_model = PandasModel(df)
            self.productos_table.setModel(self.productos_model)
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            # Si falla, mostrar un modelo vacío o un mensaje
            self.productos_model = PandasModel(pd.DataFrame())
            self.productos_table.setModel(self.productos_model)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def total_calzados(self):
        """Calcula y muestra el total de calzados agrupados."""
        try:
            grupal = ventas_x_categoria_grupal()
            grupal_str = grupal.to_string()  # Convertir a string
            self.total_label.setText(grupal_str)
            self.total_label.adjustSize()
        except Exception as e:
            print(f"Error al calcular el total de calzados: {e}")
            self.total_label.setText("No se pudo calcular el total")
