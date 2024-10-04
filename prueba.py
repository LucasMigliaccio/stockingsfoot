import pandas as pd

# Cargar los datos
df_calzados = pd.read_excel("archivos/Transacciones de venta_638619535650617648.xlsx")
df_medias = pd.read_excel("archivos/Transacciones de venta_638619537133694463.xlsx")

# Opciones para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)  
#pd.set_option('display.max_columns', None)

# Convertir la columna "Grupo de ventas" a numérico (int)
df_calzados["Grupo de ventas"] = pd.to_numeric(df_calzados["Grupo de ventas"], errors='coerce')


# Filtrar por el valor numérico 13319
filtro_ventas = df_calzados[df_calzados["Grupo de ventas"] == 13319]
# Mostrar el filtro
print(filtro_ventas)


# Agrupar por 'Grupo de ventas' y sumar la cantidad de calzados vendidos
ventas_calzados_por_grupo = df_calzados.groupby("Grupo de ventas")["Cantidad"].sum()
print(ventas_calzados_por_grupo)

ventas_medias_por_grupo = df_medias.groupby("Grupo de ventas")["Cantidad"].sum()
print(ventas_medias_por_grupo)

porcentaje = (ventas_medias_por_grupo / ventas_calzados_por_grupo) * 100
for grupo, valor in porcentaje.items():
    print(f"Grupo de ventas = {grupo}    % {valor:.2f}")
#Filtrar I = CANTIDAD / J = GRUPO DE VENTAS


# Verificar las columnas y tipos de datos (descomentar si es necesario)
# print(df_calzados.columns)
# print(df_calzados.dtypes)

# Ver los valores únicos en la columna
#print(df_calzados["Grupo de ventas"].unique())  # Mostrar valores únicos de la columna "Grupo de ventas"