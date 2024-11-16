import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.marcas_favoritas_individual import ViewMarcaIndividual
from database.queries_calzado import ventas_x_marca_individual

from models.producto import PandasModel

data_marca = ventas_x_marca_individual()

df_marca = pd.DataFrame(data_marca)
df_marca.iloc[:, 2:] = df_marca.iloc[:, 2:].abs()

class ViewMarcaIndividualForm(QWidget, ViewMarcaIndividual):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.marcas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.marca_model = PandasModel(df_marca)
        self.marcas_table.setModel(self.marca_model) 

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)