import pandas as pd
from tkinter import filedialog

def exportar_a_excel(data):
    try:
        # Definir nombres de columnas
        columns = ["idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "bebidas_fin_semana",
                   "bebidas_destiladas_semana", "vinos_semana", "perdidas_control", "diversion_dependencia_alcohol",
                   "problemas_digestivos", "tension_alta", "dolor_cabeza"]

        # Crear el DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Abrir diálogo para elegir la ubicación de guardado
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])
        if file_path:
            # Exportar datos a Excel
            df.to_excel(file_path, index=False)
            print(f"Datos exportados a {file_path}")
    except Exception as e:
        # Manejar error al exportar datos
        print(f"Error al exportar datos: {e}")