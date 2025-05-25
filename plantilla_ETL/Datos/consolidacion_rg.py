import pandas as pd
import glob
import os

# Carpeta donde están los archivos CSV originales
carpeta_csv = "./CSV/RG" #Cambiar a ./CSV/USH

# Buscar todos los archivos .csv en la carpeta
archivos = glob.glob(os.path.join(carpeta_csv, "*.csv"))

# Leer todos los CSV sin encabezado, usando ',' como separador de columnas y '.' como separador decimal
dataframes = [pd.read_csv(archivo, sep=',', decimal='.', header=0) for archivo in archivos]

# Quitar encabezado original releyendo todos los archivos desde la segunda fila
dataframes_sin_encabezado = [pd.read_csv(archivo, sep=',', decimal='.', header=None, skiprows=1) for archivo in archivos]

# Combinar todos los DataFrames
df_combinado = pd.concat(dataframes_sin_encabezado, ignore_index=True)

# Asignar encabezado personalizado
df_combinado.columns = ['Proveedor', 'Producto', 'Fecha', 'Precio']

# Ruta del archivo combinado de salida
archivo_salida = os.path.join(carpeta_csv, "./CONSOLIDADO/archivo_combinado2024_2025.csv")

# Guardar usando ';' como separador de columnas y ',' como separador decimal
df_combinado.to_csv(archivo_salida, index=False, sep=';', decimal=',')

print(f"Archivos combinados exitosamente.")
