import pandas as pd

# Cargar los datos
df_calzados = pd.read_excel("archivos/Transacciones de venta_638619535650617648.xlsx")
df_medias = pd.read_excel("archivos/Transacciones de venta_638619537133694463.xlsx")

# Opciones para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)  
#pd.set_option('display.max_columns', None)

# Verificar las columnas y tipos de datos (descomentar si es necesario)
# print(df_calzados.columns)
# print(df_calzados.dtypes)

# Convertir la columna "Grupo de ventas" a numérico (int)
df_calzados["Grupo de ventas"] = pd.to_numeric(df_calzados["Grupo de ventas"], errors='coerce')

# Ver los valores únicos en la columna
#print(df_calzados["Grupo de ventas"].unique())  # Mostrar valores únicos de la columna "Grupo de ventas"

# Filtrar por el valor numérico 13319
filtro_ventas = df_calzados[df_calzados["Grupo de ventas"] == 13319]

# Mostrar el filtro
print(filtro_ventas)
#df_calzados.to_excel('archivo_modificado.xlsx', index=False)

#Filtrar I = CANTIDAD / J = GRUPO DE VENTAS