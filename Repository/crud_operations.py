from .conexion_bd import conectar, cerrar_conexion

def agregar_encuesta(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza))
            conexion.commit()
        except Exception as e:
            print(f"Error al agregar encuesta: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_encuestas():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza FROM ENCUESTA")
            rows = cursor.fetchall()
            print(f"Database rows: {rows}")  # Debug print
            return rows
        except Exception as e:
            print(f"Error al obtener encuestas: {e}")
            return []
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return []

def actualizar_encuesta(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza, id_encuesta):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE ENCUESTA
                SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s
                WHERE idEncuesta=%s
            """, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza, id_encuesta))
            conexion.commit()
        except Exception as e:
            print(f"Error al actualizar encuesta: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_encuesta(id_encuesta):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (id_encuesta,))
            conexion.commit()
        except Exception as e:
            print(f"Error al eliminar encuesta: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)