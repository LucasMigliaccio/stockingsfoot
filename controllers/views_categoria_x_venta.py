import os
import pandas as pd
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.ventas_x_categoria_individual import ViewProductos

from database.queries_calzado import ventas_x_categoria_individual, ventas_x_categoria_grupal

from models.producto import PandasModel


data = ventas_x_categoria_individual()

df = pd.DataFrame(data)
df.iloc[:, 1:] = df.iloc[:, 1:].abs() 

class ViewCategoriasForm(QWidget, ViewProductos):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.productos_table.setSelectionBehavior(QAbstractItemView.SelectRows) 

        self.productos_model = PandasModel(df)
        self.productos_table.setModel(self.productos_model)
        self.total_calzados()

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def total_calzados(self):
        grupal= ventas_x_categoria_grupal()
        grupal_str = grupal.to_string()
        self.total_label.setText(grupal_str)
        self.total_label.adjustSize()
