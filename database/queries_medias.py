import sqlite3
import pandas as pd
from .database import get_connection

def obtener_datos_medias():
    conn = get_connection()
    query = "SELECT * FROM ventas_medias;"
    df_medias = pd.read_sql_query(query, conn)
    conn.close()
    return df_medias


def obtener_medias_filtradas():
    conn = get_connection()
    query = """SELECT "Grupo de ventas", SUM(Cantidad) AS TotalCantidad
                FROM ventas_medias
                WHERE Categoría LIKE '%med%'
                GROUP BY "Grupo de ventas";"""
    df_medias_filtradas = pd.read_sql_query(query, conn)
    conn.close()
    return df_medias_filtradas