import sqlite3
import os

# Número de tienda
# Fecha
# Hora de la transacción
# Categoría	
# Código de artículo
# Nombre del producto
# Tamaño
# Almacén	
# Cantidad	
# Grupo de ventas
# Importe antes de impuestos	
# Número de recibo
# Id. de operador 

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), "ventas.sqlite3")
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"No se encontró el archivo de base de datos en {db_path}")
    conn = sqlite3.connect(db_path)
    return conn

def check_table_exists(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    cursor.execute(query)
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def create_tables_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    if not check_table_exists("ventas_calzado"):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas_calzado (
        "Número de tienda" INTEGER,
        "Fecha" TEXT,
        "Hora de la transacción" TEXT,
        "Categoría" TEXT,
        "Código de artículo" TEXT,
        "Nombre del producto" TEXT,
        "Tamaño" TEXT,
        "Almacén" INTEGER,
        "Cantidad" INTEGER,
        "Grupo de ventas" INTEGER,
        "Importe antes de impuestos" REAL,
        "Número de recibo" TEXT,
        "Id. de operador" INTEGER,
        "Importe del pago" REAL
    );
        """)
    if not check_table_exists("ventas_medias"):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas_medias (
        "Número de tienda" INTEGER,
        "Fecha" TEXT,
        "Hora de la transacción" TEXT,
        "Categoría" TEXT,
        "Código de artículo" TEXT,
        "Nombre del producto" TEXT,
        "Tamaño" TEXT,
        "Almacén" INTEGER,
        "Cantidad" INTEGER,
        "Grupo de ventas" INTEGER,
        "Importe antes de impuestos" REAL,
        "Número de recibo" TEXT,
        "Id. de operador" INTEGER,
        "Importe del pago" REAL
    );
        """)
    conn.commit()
    conn.close()


def create_ventas_calzado_table():
    conn = get_connection()
    cursor = conn.cursor()
    query = query = '''
    CREATE TABLE IF NOT EXISTS ventas_calzado (
        "Número de tienda" INTEGER,
        "Fecha" TEXT,
        "Hora de la transacción" TEXT,
        "Categoría" TEXT,
        "Código de artículo" TEXT,
        "Nombre del producto" TEXT,
        "Tamaño" TEXT,
        "Almacén" INTEGER,
        "Cantidad" REAL,
        "Grupo de ventas" INTEGER,
        "Importe antes de impuestos" REAL,
        "Número de recibo" TEXT,
        "Id. de operador" INTEGER,
        "Importe del pago" REAL
    );
'''
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("Tabla venta_calzado creada o ya existente.")

def create_ventas_medias_table():
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS ventas_medias (
        "Número de tienda" INTEGER,
        "Fecha" TEXT,
        "Hora de la transacción" TEXT,
        "Categoría" TEXT,
        "Código de artículo" TEXT,
        "Nombre del producto" TEXT,
        "Tamaño" TEXT,
        "Almacén" INTEGER,
        "Cantidad" INTEGER,
        "Grupo de ventas" INTEGER,
        "Importe antes de impuestos" REAL,
        "Número de recibo" TEXT,
        "Id. de operador" INTEGER,
        "Importe del pago" REAL
    );
    '''
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("Tabla ventas_medias creada o ya existente.")


def clean_database_calzados():
    conn = get_connection()
    cursor = conn.cursor()
    query="""DELETE FROM ventas_calzado;"""
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("TABLA CALZADOS LIMPIA")

def clean_database_medias():
    conn = get_connection()
    cursor = conn.cursor()
    query="""DELETE FROM ventas_medias;"""
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("TABLA CALZADOS LIMPIA")