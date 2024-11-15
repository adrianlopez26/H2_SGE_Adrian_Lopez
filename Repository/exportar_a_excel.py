import pandas as pd
from tkinter import filedialog

def exportar_a_excel(data):
    try:
        # Define column names
        columns = ["idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "bebidas_fin_semana",
                   "bebidas_destiladas_semana", "vinos_semana", "perdidas_control", "diversion_dependencia_alcohol",
                   "problemas_digestivos", "tension_alta", "dolor_cabeza"]

        # Create a DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Open file dialog to choose save location
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            df.to_excel(file_path, index=False)
            print(f"Datos exportados a {file_path}")
    except Exception as e:
        print(f"Error al exportar datos: {e}")