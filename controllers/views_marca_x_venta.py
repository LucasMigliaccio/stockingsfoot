import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.ventas_x_genero_grupal import ViewGenero
from database.queries_calzado import ventas_x_genero_grupal


class ViewGeneroForm(QWidget, ViewGenero):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


