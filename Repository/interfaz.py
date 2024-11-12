import tkinter as tk
from tkinter import ttk
from conexion_bd import conectar


class AppEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Encuestas")
        self.geometry("800x600")

        # Campos de entrada para la encuesta
        tk.Label(self, text="Edad:").grid(row=0, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(self)
        self.edad_entry.grid(row=0, column=1)

        tk.Label(self, text="Sexo:").grid(row=1, column=0, padx=10, pady=5)
        self.sexo_entry = tk.Entry(self)
        self.sexo_entry.grid(row=1, column=1)

        tk.Label(self, text="Bebidas por Semana:").grid(row=2, column=0, padx=10, pady=5)
        self.bebidas_semana_entry = tk.Entry(self)
        self.bebidas_semana_entry.grid(row=2, column=1)

        tk.Label(self, text="Cervezas por Semana:").grid(row=3, column=0, padx=10, pady=5)
        self.cervezas_semana_entry = tk.Entry(self)
        self.cervezas_semana_entry.grid(row=3, column=1)

        # Agrega más entradas para otros campos como BebidasFinSemana, etc.
        tk.Label(self, text="Bebidas de Fin de Semana:").grid(row=4, column=0, padx=10, pady=5)
        self.bebidas_fin_semana_entry = tk.Entry(self)
        self.bebidas_fin_semana_entry.grid(row=4, column=1)

        tk.Label(self, text="Pérdidas de Control:").grid(row=5, column=0, padx=10, pady=5)
        self.perdidas_control_entry = tk.Entry(self)
        self.perdidas_control_entry.grid(row=5, column=1)

        # Botones de acciones
        tk.Button(self, text="Agregar Encuesta", command=self.agregar_encuesta).grid(row=6, column=0, pady=10)
        tk.Button(self, text="Ver Encuestas", command=self.ver_encuestas).grid(row=6, column=1)

        # Tabla para mostrar los registros
        self.tree = ttk.Treeview(self, columns=(
        "idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "perdidas_control"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=7, column=0, columnspan=4)

    def agregar_encuesta(self):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            edad = self.edad_entry.get()
            sexo = self.sexo_entry.get()
            bebidas_semana = self.bebidas_semana_entry.get()
            cervezas_semana = self.cervezas_semana_entry.get()
            bebidas_fin_semana = self.bebidas_fin_semana_entry.get()
            perdidas_control = self.perdidas_control_entry.get()

            cursor.execute("""
                INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, PerdidasControl)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, perdidas_control))

            conexion.commit()
            print("Encuesta añadida correctamente.")
            cursor.close()
            conexion.close()

    def ver_encuestas(self):
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, PerdidasControl FROM ENCUESTA")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
            cursor.close()
            conexion.close()


if __name__ == "__main__":
    app = AppEncuestas()
    app.mainloop()
