import pandas as pd
import glob
import os

# Ruta de la carpeta que contiene los archivos .xlsx
ruta = "./RIO GRANDE/2025"   #Ajustar Ruta y Cambiar a Ushuaia

# Buscar todos los archivos .xlsx en la carpeta
archivos = glob.glob(os.path.join(ruta, "*.xlsx"))

# Leer y combinar todos los archivos en un solo DataFrame
df_completo = pd.concat([pd.read_excel(archivo) for archivo in archivos], ignore_index=True)

# Asegurarse de que la columna 'fecha' es texto (por si es datetime)
df_completo['fecha'] = df_completo['fecha'].astype(str)

# Eliminar la hora, dejando solo la parte de la fecha (antes del espacio)
df_completo['fecha'] = df_completo['fecha'].str.split(' ').str[0]

# Eliminar la columna 'operador'
df_completo.drop(columns='operador', inplace=True)

# Filtrar los precios: eliminar filas con precio > 70000.0
df_completo = df_completo[df_completo['precio'] <= 70000.0]

# Crear la carpeta de destino si no existe
salida = "./CSV/RG" #Cambiar a ./CSV/USH
os.makedirs(salida, exist_ok=True)

# Guardar el DataFrame como CSV en la carpeta de salida
df_completo.to_csv(os.path.join(salida, "Archivo_conversion_2025.csv"), index=False)

print("Archivos combinados, filtrados y guardados en './CSV/archivo_conversion_2025.csv'")
