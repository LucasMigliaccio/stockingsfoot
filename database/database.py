import sqlite3
import os

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), "ventas.sqlite3")
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"No se encontró el archivo de base de datos en {db_path}")
    conn = sqlite3.connect(db_path)
    return conn

def check_table_exists(table_name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    cursor.execute(query)
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def create_tables_if_not_exists():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if not check_table_exists("ventas_calzado"):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas_calzado (
        "Numero de tienda" INTEGER,
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
        """)
    if not check_table_exists("ventas_medias"):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas_medias (
        "Numero de tienda" INTEGER,
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
        """)
    conn.commit()
    conn.close()


def create_ventas_calzado_table():
    conn = get_connection()
    cursor = conn.cursor()
    query = query = '''
    CREATE TABLE IF NOT EXISTS ventas_calzado (
        "Numero de tienda" INTEGER,
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
        "Numero de tienda" INTEGER,
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
    print("Tabla ventas_medias creada o ya existente.")
