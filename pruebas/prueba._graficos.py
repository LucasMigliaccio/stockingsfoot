from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel
import pyqtgraph as pg
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

class MainWindow(QMainWindow):
    def __init__(self, data_frame):
        super().__init__()
        self.setWindowTitle("Gráfico de Barras Apiladas Horizontal con PyQtGraph")
        self.setGeometry(100, 100, 800, 600)

        # Configurar el widget central y el layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Crear el widget de gráfico
        plot_widget = pg.PlotWidget()
        layout.addWidget(plot_widget)

        # Extraer las categorías (columnas) excluyendo "Grupo de ventas"
        categorias = data_frame.columns[1:]
        y_positions = range(len(data_frame))  # Posiciones en el eje Y para cada grupo de ventas
        x_offset = [0] * len(data_frame)  # Acumulador para apilar las cantidades en el eje X

        # Colores para cada categoría
        colores = [pg.intColor(i, len(categorias)) for i in range(len(categorias))]

        # Graficar cada categoría como una barra apilada
        for i, categoria in enumerate(categorias):
            cantidades = data_frame[categoria].values  # Cantidades para la categoría actual
            bar = pg.BarGraphItem(y=y_positions, x0=x_offset, height=0.2, width=cantidades, brush=colores[i])
            plot_widget.addItem(bar)
            # Actualizar el offset en x para la próxima categoría (apilado)
            x_offset = [x + cantidad for x, cantidad in zip(x_offset, cantidades)]

        # Configurar etiquetas y ejes
        plot_widget.getAxis('left').setTicks([[(i, str(name)) for i, name in enumerate(data_frame["Grupo de ventas"])]])
        plot_widget.setLabel('bottom', 'Cantidad')
        plot_widget.setLabel('left', 'Grupo de ventas')

        # Crear una leyenda para mostrar los colores y categorías
        legend_layout = QHBoxLayout()
        layout.addLayout(legend_layout)

        for i, categoria in enumerate(categorias):
            color_label = QLabel()
            color_label.setFixedSize(15, 15)
            color_label.setStyleSheet(f"background-color: {colores[i].name()};")  # Utilizar .name() directamente
            legend_layout.addWidget(color_label)
            legend_layout.addWidget(QLabel(categoria))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear la ventana principal y pasar el DataFrame
    main_window = MainWindow(df)
    main_window.show()

    sys.exit(app.exec())
