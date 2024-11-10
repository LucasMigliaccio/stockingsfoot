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
    query = """SELECT "Categoría", SUM(Cantidad) AS "Total Cantidad" FROM ventas_calzado GROUP BY "Categoría";"""
    df_calzados_filtrados_genero = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados_filtrados_genero


def ventas_x_categoria_individual():
    conn = get_connection()
    query_categorias = 'SELECT DISTINCT "Categoría" FROM ventas_calzado'
    categorias = pd.read_sql(query_categorias, conn)["Categoría"].tolist()

    # Paso 2: Construir la consulta SQL dinámica
    select_clause = '"Grupo de ventas", ' + ', '.join(
        [f'SUM(CASE WHEN "Categoría" = "{categoria}" THEN "Cantidad" ELSE 0 END) AS "{categoria}"'
        for categoria in categorias]
    )
    query = f'SELECT {select_clause} FROM ventas_calzado GROUP BY "Grupo de ventas";'
    resultado = pd.read_sql(query, conn)
    conn.close()
    return resultado

def ventas_x_categoria_grupal():
    conn = get_connection()
    query = """SELECT "Categoría", SUM("Cantidad") AS "Total Cantidad"
                FROM ventas_calzado
                GROUP BY "Categoría";"""
    df_calzados_grupal = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados_grupal


def producto_mas_vendido():
    conn = get_connection()
    query = """SELECT 
            SUBSTR("Nombre del producto", INSTR("Nombre del producto", ' ') + 1) AS "Marca",
            SUM("Cantidad") AS "Total Cantidad"
            FROM ventas_calzado
            GROUP BY "Marca";
            """
    df_genero_grupal = pd.read_sql_query(query, conn)
    conn.close()
    return df_genero_grupal


def calzados_mas_vendidos():
    conn = get_connection()
    query ="""SELECT 
            SUBSTR("Nombre del producto", INSTR("Nombre del producto", ' ') + 1) AS "Calzados", ("Código de artículo"),
            SUM("Cantidad") AS "Total Cantidad"
            FROM ventas_calzado
            GROUP BY "Calzados"
            ORDER BY "Total Cantidad" ASC
            LIMIT 10;"""
    df_calzados_mas_vendidos = pd.read_sql_query(query, conn)
    conn.close()
    return df_calzados_mas_vendidos


def genero_mas_vendido():
    conn = get_connection()
    query ="""SELECT 
            SUBSTR("Categoría", INSTR("Categoría", ' ') + 1) AS "Género",
            SUM("Cantidad") AS "Total Cantidad"
            FROM ventas_calzado
            GROUP BY "Género";
            """
    df_generos_mas_vendidos = pd.read_sql_query(query, conn)
    conn.close()
    return df_generos_mas_vendidos