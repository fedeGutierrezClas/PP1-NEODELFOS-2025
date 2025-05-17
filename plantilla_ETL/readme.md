# 🛠️ Proyecto Neodelfos - Plantilla ETL

Este proyecto es una **plantilla base para procesos ETL** (Extract, Transform, Load) sobre archivos Excel con datos de distintas localidades (RIO GRANDE y USHUAIA). Permite organizar y procesar datos crudos, transformarlos según reglas de negocio, y exportar resultados listos para análisis o reportes.

---

## 📁 Estructura del proyecto

proyecto_Neodelfos                             ← Carpeta madre
└plantilla_ETL/                                ← Carpeta contenedora del proyecto
 ├── Datos/                                    ← Carpeta contenedora de datos del proyecto
 │   ├── Crudos/                               ← Datos sin procesar
 │   │   ├── RIO GRANDE ENERO 2025.xlsx
 │   │   ├── RIO GRANDE FEBRERO 2025.xlsx
 │   │   ├── RIO GRANDE MARZO 2025.xlsx
 │   │   ├── RIO GRANDE TODO 2024.xlsx
 │   │   ├── USHUAIA ENERO 2025.xlsx
 │   │   ├── USHUAIA FEBRERO 2025.xlsx
 │   │   ├── USHUAIA MARZO 2025.xlsx
 │   │   └── USHUAIA TODO 2024.xlsx
 │   ├── WIP/                                  ← Datos en proceso (Work In Progress)
 │   └── Finalizado/                           ← Datos procesados
 ├── Documentos/                               ← Documentación del proyecto
 ├── Informes/                                 ← Informes de cambios de versión
 │   └── Version 1.0.txt
 ├── readme.md                                 ← Explicación del proyecto (Usted se encuentra aquí)
 └── requirements.txt                          ← Librerías utilizadas en el proyecto