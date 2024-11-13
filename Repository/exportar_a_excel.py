# File: exportar_a_excel.py
import pandas as pd
from sqlalchemy import create_engine
from tkinter import filedialog
from .conexion_bd import conectar

def exportar_a_excel():
    conexion = conectar()
    if conexion:
        try:
            # Create SQLAlchemy engine
            engine = create_engine(f"mysql+pymysql://root:curso@localhost/encuestas")
            query = "SELECT * FROM ENCUESTA"
            df = pd.read_sql(query, engine)

            # Open file dialog to choose save location
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                df.to_excel(file_path, index=False)
                print(f"Datos exportados a {file_path}")
        except Exception as e:
            print(f"Error al exportar datos: {e}")
        finally:
            conexion.close()