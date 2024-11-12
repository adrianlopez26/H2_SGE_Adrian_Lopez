import pandas as pd
from .conexion_bd import conectar

def exportar_a_excel():
    conexion = conectar()
    if conexion:
        query = "SELECT * FROM ENCUESTA"
        df = pd.read_sql(query, conexion)
        df.to_excel("encuestas.xlsx", index=False)
        print("Datos exportados a encuestas.xlsx")
        conexion.close()