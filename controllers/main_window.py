from PySide6.QtWidgets import QWidget, QFileDialog, QVBoxLayout

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi

import pandas as pd

class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.init_ui()

        self.recuento_button.clicked.connect(self.procesar_archivos)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def init_ui(self):
        # Configuramos el layout
        layout = QVBoxLayout()

        # Creamos el botón
        self.medias_pushButton.clicked.connect(self.abrir_medias_archivos)
        self.pushButton.clicked.connect(self.abrir_calzados_archivos)

        # Configuramos la ventana principal
        self.setLayout(layout)
        self.setWindowTitle("Ejemplo QFileDialog")

    def abrir_archivo(self, tipo_archivo):
        # Abrimos un QFileDialog cuando se presiona el botón
        archivo, _ = QFileDialog.getOpenFileName(self, f"Seleccionar archivo de {tipo_archivo}", "", "Todos los archivos (*)")
        
        if archivo:
            # Verificamos qué tipo de archivo es y guardamos en una variable
            if tipo_archivo == "MEDIAS":
                self.medias_archivo = archivo  # Guardamos el archivo seleccionado de medias
            elif tipo_archivo == "CALZADOS":
                self.calzados_archivo = archivo  # Guardamos el archivo seleccionado de calzados
            
            # Actualizamos el texto del label con ambos archivos seleccionados (si existen)
            medias_text = f"MEDIAS: {self.medias_archivo}" if hasattr(self, 'medias_archivo') else "MEDIAS: No seleccionado"
            calzados_text = f"CALZADOS: {self.calzados_archivo}" if hasattr(self, 'calzados_archivo') else "CALZADOS: No seleccionado"
            
            # Actualizamos el label con ambos archivos seleccionados
            self.porcentajes_label.setText(f"{medias_text}\n{calzados_text}")
            self.porcentajes_label.adjustSize()

    # Para abrir archivos de medias
    def abrir_medias_archivos(self):
        self.abrir_archivo("MEDIAS")

    # Para abrir archivos de calzados
    def abrir_calzados_archivos(self):
        self.abrir_archivo("CALZADOS")
        
    def procesar_archivos(self):
        try:
            if hasattr(self, 'medias_archivo'):
                # Cargar el archivo de medias en un DataFrame
                df_medias = pd.read_excel(self.medias_archivo)

                # Filtrar solo las filas donde 'Categoría' contiene la palabra "med"
                df_medias_filtrado = df_medias[df_medias['Categoría'].str.contains('med', case=False, na=False)]

                # Agrupar por 'Grupo de ventas' y sumar la columna 'Cantidad'
                fila_legajos_medias = df_medias_filtrado.groupby("Grupo de ventas")['Cantidad'].sum()
                print("MEDIAS FILTRADAS \n", fila_legajos_medias)

            if hasattr(self, 'calzados_archivo'):
                # Cargar el archivo de calzados en un DataFrame
                df_calzados = pd.read_excel(self.calzados_archivo)  # O pd.read_excel() si es un archivo Excel
                fila_legajos_calzados = df_calzados.groupby("Grupo de ventas")['Cantidad'].sum()
                print("CALZADOS \n", fila_legajos_calzados)

            # Realizar el merge entre calzados y medias
            resultado = pd.merge(fila_legajos_calzados, fila_legajos_medias, on='Grupo de ventas', how='left')
            resultado.columns = ['Calzados', 'Medias']
            resultado.index.name = ""

            # Filtro para evitar valores nulos
            resultado = resultado.dropna(subset=['Calzados', 'Medias'])

            # Calcular el porcentaje de medias respecto a calzados
            resultado['%'] = (resultado['Medias'] / resultado['Calzados']) * 100

            # Convertir el DataFrame a texto para mostrarlo en el QLabel
            resultado_str = resultado.to_string()

            # Mostrar el DataFrame en el QLabel
            self.porcentajes_label.setText(resultado_str)
            self.porcentajes_label.adjustSize()

            print(resultado)

        except Exception as e:
            print(f"Error al procesar los archivos: {e}")
            self.porcentajes_label.setText("Error al procesar los archivos.")
            self.porcentajes_label.adjustSize()

    def ceo_analitica(self):
        pass

