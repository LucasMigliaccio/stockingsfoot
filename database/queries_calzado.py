import sqlite3
import pandas as pd
from .database import get_connection


def obtener_datos_calzados():
    conn = get_connection()
    query = "SELECT * FROM ventas_calzado;"
    df_calzados = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados


def obtener_calzados_filtrados():
    conn = get_connection()
    query = """SELECT "Grupo de ventas", SUM(Cantidad) AS TotalCantidad FROM ventas_calzado GROUP BY "Grupo de ventas";"""
    df_calzados_filtrados = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados_filtrados


def total_calzados_filtrados_genero():
    conn = get_connection()
    query = """SELECT "Categoría", SUM(Cantidad) AS TotalCantidad FROM ventas_calzado GROUP BY "Categoría";"""
    df_calzados_filtrados_genero = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados_filtrados_genero