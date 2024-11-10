import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

# Supongamos que tenemos el DataFrame de géneros y cantidades
data = {
    "Género": ["Hombre", "Mujer", "Niña", "Niño", "Unisex"],
    "Cantidad": [30, 15, 7, 17, 18]
}
df = pd.DataFrame(data)

class GraficoWidget(QWidget):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.df = df
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Crear la figura y el canvas para matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        canvas = FigureCanvas(fig)
        
        # Graficar el DataFrame
        ax.barh(self.df["Género"], self.df["Cantidad"], color="skyblue")
        ax.set_xlabel("Cantidad")
        ax.set_ylabel("Género")
        ax.set_title("Cantidad por Género de Calzado")
        
        # Añadir el canvas al layout
        layout.addWidget(canvas)
        canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con Gráfico en Pestaña")

        # Crear el tab widget
        tab_widget = QTabWidget(self)
        self.setCentralWidget(tab_widget)
        
        # Pestaña del gráfico
        grafico_tab = GraficoWidget(df)
        tab_widget.addTab(grafico_tab, "Gráfico de Género")

# Configurar y ejecutar la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.resize(800, 600)
window.show()
sys.exit(app.exec())
