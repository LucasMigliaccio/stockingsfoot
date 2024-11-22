from PySide6.QtWidgets import QWidget, QFileDialog, QVBoxLayout
from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
import pandas as pd
import sqlite3

from database.database import get_connection, create_ventas_calzado_table, create_ventas_medias_table, check_table_exists, create_tables_if_not_exists
from database.queries_calzado import obtener_datos_calzados, obtener_calzados_filtrados, ventas_x_categoria_individual
from database.queries_medias import obtener_datos_medias, obtener_medias_filtradas

from controllers.views_categoria_x_venta import ViewCategoriasForm
from controllers.views_genero_x_venta import ViewGeneroForm
from controllers.views_calzados_marca_mas_vendidos import ViewMarcaoForm
from controllers.views_marca_x_venta_individual import ViewMarcaIndividualForm

class MainWindowForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.init_ui()

        # Crear tablas si no existen
        create_tables_if_not_exists()

        # Conectar botones
        self.recuento_button.clicked.connect(self.procesar_archivos)
        self.categorias_vendidas_button.clicked.connect(self.open_categorias_analitica)
        self.genero_button.clicked.connect(self.open_genero_analitica)
        self.marca_button.clicked.connect(self.open_marcacalzado_analitica)
        self.marcafav_button.clicked.connect(self.open_marcacalzado_individual_analitica)

        
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def init_ui(self):
        layout = QVBoxLayout()
        self.medias_pushButton.clicked.connect(self.abrir_medias_archivos)
        self.calzados_pushButton.clicked.connect(self.abrir_calzados_archivos)
        self.setLayout(layout)
        self.setWindowTitle("Ejemplo QFileDialog")

    def abrir_archivo(self, tipo_archivo):
        archivo, _ = QFileDialog.getOpenFileName(self, f"Seleccionar archivo de {tipo_archivo}", "", "Archivos Excel (*.xlsx)")
        
        if archivo:
            self.convertir_excel_a_sqlite(archivo, tipo_archivo)
            if tipo_archivo == "MEDIAS":
                self.medias_archivo = archivo
            elif tipo_archivo == "CALZADOS":
                self.calzados_archivo = archivo
            self.actualizar_label()

    def actualizar_label(self):
        medias_text = f"MEDIAS: {self.medias_archivo}" if hasattr(self, 'medias_archivo') else "MEDIAS: No seleccionado"
        calzados_text = f"CALZADOS: {self.calzados_archivo}" if hasattr(self, 'calzados_archivo') else "CALZADOS: No seleccionado"
        self.porcentajes_label.setText(f"{medias_text}\n{calzados_text}")
        self.porcentajes_label.adjustSize()

    def procesar_archivos(self):
        try:
            if not (check_table_exists("ventas_calzado") and check_table_exists("ventas_medias")):
                raise ValueError("No se encontraron las tablas necesarias en la base de datos.")

            df_medias = obtener_calzados_filtrados()
            df_calzados = obtener_medias_filtradas()

            # Realiza el merge y demás operaciones como antes
            df_medias_y_calzados = pd.merge(df_calzados, df_medias, on='Grupo de ventas', how='left')
            # Continúa con las operaciones...
            df_medias_y_calzados = df_medias_y_calzados.rename(columns={'TotalCantidad_x': 'Medias', 'TotalCantidad_y': 'Calzados'})
            #resultado.columns = ['Calzados', 'Medias']
            df_medias_y_calzados.index.name = ""

            # Filtro para evitar valores nulos
            df_medias_y_calzados = df_medias_y_calzados.dropna(subset=['Calzados', 'Medias'])

            # Calcular el porcentaje de medias respecto a calzados
            df_medias_y_calzados['%'] = (df_medias_y_calzados['Medias'] / df_medias_y_calzados['Calzados']) * 100
            df_medias_y_calzados['%'] = df_medias_y_calzados['%'].round(1).astype(str) + '%'

            # Convertir el DataFrame a texto para mostrarlo en el QLabel
            df_medias_y_calzados_str = df_medias_y_calzados.to_string()

            # Mostrar el DataFrame en el QLabel
            self.porcentajes_label.setText(df_medias_y_calzados_str)
            self.porcentajes_label.adjustSize()

            print(df_medias_y_calzados)

        except Exception as e:
            print(f"Error al procesar los archivos: {e}")
            self.porcentajes_label.setText("Error al procesar los archivos.")
            self.porcentajes_label.adjustSize()

    def convertir_excel_a_sqlite(self, archivo, tipo_archivo):
        df = pd.read_excel(archivo)
        conn = sqlite3.connect("database.db")
        try:
            table_name = "ventas_medias" if tipo_archivo == "MEDIAS" else "ventas_calzado"
            if not check_table_exists(table_name):
                df.to_sql(table_name, conn, if_exists='replace', index=False)
            else:
                # Verifica si la tabla ya contiene datos
                cursor = conn.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                if count == 0:
                    df.to_sql(table_name, conn, if_exists='replace', index=False)
                else:
                    print(f"Tabla {table_name} ya contiene datos. Salteando carga.")
        except Exception as e:
            print(f"Error al convertir Excel a SQLite: {e}")
        finally:
            conn.close()


    def abrir_medias_archivos(self):
        self.abrir_archivo("MEDIAS")

    def abrir_calzados_archivos(self):
        self.abrir_archivo("CALZADOS")

    def open_categorias_analitica(self):
        window= ViewCategoriasForm(self)
        window.show()

    def open_genero_analitica(self):
        window= ViewGeneroForm(self)
        window.show()
    
    def open_marcacalzado_analitica(self):
        window= ViewMarcaoForm(self)
        window.show()
        
    def open_marcacalzado_individual_analitica(self):
        window= ViewMarcaIndividualForm(self)
        window.show()