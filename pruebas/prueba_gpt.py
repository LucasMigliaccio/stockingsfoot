import sqlite3
import os
import pandas as pd

# Ruta de la base de datos


#FILTRO DE CATEGORIAS Y POSTERIOR CONVERSION A DATAFRAME
DB_PATH = os.path.join(os.path.dirname(__file__), 'app_data.db')

def get_connection():
    db_path = os.path.join("database", "ventas.sqlite3")
    conn = sqlite3.connect(db_path)
    return conn
    
conn = get_connection()

# Paso 1: Obtener las categorías únicas
query_categorias = 'SELECT DISTINCT "Categoría" FROM ventas_calzado'
categorias = pd.read_sql(query_categorias, conn)["Categoría"].tolist()

# Paso 2: Construir la consulta SQL dinámica
select_clause = '"Grupo de ventas", ' + ', '.join(
    [f'SUM(CASE WHEN "Categoría" = "{categoria}" THEN "Cantidad" ELSE 0 END) AS "{categoria}"'
     for categoria in categorias]
)
query = f'SELECT {select_clause} FROM ventas_calzado GROUP BY "Grupo de ventas";'

# Paso 3: Ejecutar la consulta y obtener los resultados
resultado = pd.read_sql(query, conn)

# Mostrar el resultado
print(resultado)

# Cerrar la conexión
conn.close()
