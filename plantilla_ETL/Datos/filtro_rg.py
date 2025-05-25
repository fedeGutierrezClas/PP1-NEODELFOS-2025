import pandas as pd
import glob
import os

# Carpeta donde están los archivos CSV originales
carpeta_csv = "./CSV/RG/CONSOLIDADO" #Cambiar a ./CSV/USH/CONSOLIDADO

# Buscar todos los archivos .csv en la carpeta
archivos = glob.glob(os.path.join(carpeta_csv, "*.csv"))

# Leer todos los CSV sin encabezado, usando ';' como separador de columnas y ',' como separador decimal
dataframes_sin_encabezado = [pd.read_csv(archivo, sep=';', decimal=',', header=None, skiprows=1) for archivo in archivos]

# Combinar todos los DataFrames
df_combinado = pd.concat(dataframes_sin_encabezado, ignore_index=True)

# Asignar encabezado personalizado
df_combinado.columns = ['Proveedor', 'Producto', 'Fecha', 'Precio']

# Convertir columna 'Precio' a numérico (por si vino como texto)
df_combinado['Precio'] = pd.to_numeric(df_combinado['Precio'], errors='coerce')

# Calcular el promedio de precio por producto
promedios = df_combinado.groupby('Producto')['Precio'].transform('mean')

# Calcular diferencia relativa absoluta entre precio y promedio
diferencia_relativa = abs(df_combinado['Precio'] - promedios) / promedios

# Filtrar filas donde la diferencia relativa sea menor o igual a 0.5 (50%)
df_filtrado = df_combinado[diferencia_relativa <= 0.5]

# Ruta del archivo combinado y filtrado de salida
carpeta_combinada = "./CSV/RG" #Cambiar a ./CSV/USH
archivo_salida = os.path.join(carpeta_combinada, "./FILTRADO/archivo_promedio.csv")

# Guardar usando ';' como separador de columnas y ',' como separador decimal
df_filtrado.to_csv(archivo_salida, index=False, sep=';', decimal=',')

print(f"Archivo combinado y filtrado guardado en '{archivo_salida}'")
