import os
import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from views.general_custom_ui import GeneralCustomUi
from views.ventas_x_genero_grupal import ViewGenero
from database.queries_calzado import ventas_x_genero_grupal

# Llamada a la consulta para obtener el DataFrame
data = ventas_x_genero_grupal()
data["Total Cantidad"] = data["Total Cantidad"].abs()  # Convertir valores negativos en positivos si los hay

class ViewGeneroForm(QWidget, ViewGenero):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        # Configurar el gráfico en la pestaña 'tab2'
        self.initGraphTab()

    def initGraphTab(self):
        # Crear una figura y un canvas para matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        canvas = FigureCanvas(fig)

        # Crear el gráfico de barras horizontal
        ax.barh(data["Género"], data["Total Cantidad"], color="skyblue")
        ax.set_xlabel("Total Cantidad")
        ax.set_ylabel("Género")
        ax.set_title("Total de Calzado por Género")

        # Añadir etiquetas de total sobre cada barra
        for index, value in enumerate(data["Total Cantidad"]):
            ax.text(value, index, f'{value}', va='center', ha='left', color="black", fontsize=10)

        # Configurar layout para la pestaña 'tab' y añadir el canvas
        layout = QVBoxLayout(self.tab)  # `tab` es la pestaña de destino
        layout.addWidget(canvas)
        canvas.draw()

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)



