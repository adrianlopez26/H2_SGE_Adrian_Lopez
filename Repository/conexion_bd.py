import pymysql
from pymysql.err import OperationalError

def conectar():
    try:
        # Establecer conexión con la base de datos
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='curso',
            database='encuestas'
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except OperationalError as e:
        # Manejar error de conexión
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion:
        # Cerrar la conexión con la base de datos
        conexion.close()
        print("Conexión cerrada")