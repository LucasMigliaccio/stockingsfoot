import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import Qt

from views.general_custom_ui import GeneralCustomUi
from views.calzados_marcas_favoritas import ViewCalzadosMarcas
from database.queries_calzado import marca_mas_vendida, calzados_mas_vendidos

from models.producto import PandasModel

class ViewMarcaForm(QWidget, ViewCalzadosMarcas):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.marcas_table.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.calzados_table.setSelectionBehavior(QAbstractItemView.SelectRows) 

        self.productos_model = None  # Inicializar vacío
        self.init_table_model()

    def init_table_model(self):
        """Inicializa el modelo de datos y lo configura en la tabla."""
        try:
            # Marca más vendida
            data_marca = marca_mas_vendida()  # Obtener datos de la consulta
            df_marca = pd.DataFrame(data_marca)  # Convertir datos a DataFrame
            df_marca.iloc[:, 1:] = df_marca.iloc[:, 1:].abs()  # Asegurar valores absolutos en columnas numéricas
            self.marca_model = PandasModel(df_marca)  # Crear modelo PandasModel
            self.marcas_table.setModel(self.marca_model)  # Configurar el modelo en la tabla
            
            # Calzados más vendidos
            data_calzados = calzados_mas_vendidos()  # Obtener datos de la consulta
            df_calzado = pd.DataFrame(data_calzados)  # Convertir datos a DataFrame
            df_calzado.iloc[:, 2:] = df_calzado.iloc[:, 2:].abs()  # Asegurar valores absolutos en columnas numéricas
            self.calzado_model = PandasModel(df_calzado)  # Crear modelo PandasModel
            self.calzados_table.setModel(self.calzado_model)  # Configurar el modelo en la tabla

        except Exception as e:
            print(f"Error al cargar datos: {e}")
            # Si falla, configurar tablas con modelos vacíos
            empty_model = PandasModel(pd.DataFrame())  # Modelo vacío
            self.marcas_table.setModel(empty_model)
            self.calzados_table.setModel(empty_model)


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)