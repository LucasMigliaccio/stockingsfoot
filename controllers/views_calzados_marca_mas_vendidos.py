import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.calzados_marcas_favoritas import ViewCalzadosMarcas
from database.queries_calzado import marca_mas_vendida, calzados_mas_vendidos

from models.producto import PandasModel

data_marca = marca_mas_vendida()
data_calzado = calzados_mas_vendidos()

df_marca = pd.DataFrame(data_marca)
df_marca.iloc[:, 1:] = df_marca.iloc[:, 1:].abs()

df_calzado = pd.DataFrame(data_calzado)
df_calzado.iloc[:, 2:] = df_calzado.iloc[:, 2:].abs() 

class ViewMarcaoForm(QWidget, ViewCalzadosMarcas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.marcas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.marca_model = PandasModel(df_marca)
        self.marcas_table.setModel(self.marca_model) 

        self.calzados_table.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.calzado_model = PandasModel(df_calzado)
        self.calzados_table.setModel(self.calzado_model)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)