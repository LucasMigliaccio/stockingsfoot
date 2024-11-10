import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.calzados_marcas_favoritas import ViewCalzadosMarcas
from database.queries_calzado import calzados_mas_vendidos


class ViewGeneroForm(QWidget, ViewCalzadosMarcas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)