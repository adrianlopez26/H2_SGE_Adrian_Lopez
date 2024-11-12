import tkinter as tk
from tkinter import ttk, messagebox
from .crud_operations import agregar_encuesta, obtener_encuestas, actualizar_encuesta, eliminar_encuesta

class AppEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Encuestas")
        self.geometry("1200x800")

        # Campos de entrada para la encuesta
        self.create_input_fields()

        # Botones de acciones
        tk.Button(self, text="Agregar Encuesta", command=self.agregar_encuesta).grid(row=12, column=0, pady=10)
        tk.Button(self, text="Ver Encuestas", command=self.ver_encuestas).grid(row=12, column=1)
        tk.Button(self, text="Actualizar Encuesta", command=self.actualizar_encuesta).grid(row=12, column=2)
        tk.Button(self, text="Eliminar Encuesta", command=self.eliminar_encuesta).grid(row=12, column=3)

        # Tabla para mostrar los registros
        self.tree = ttk.Treeview(self, columns=(
            "idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "bebidas_fin_semana",
            "bebidas_destiladas_semana", "vinos_semana", "perdidas_control", "diversion_dependencia_alcohol",
            "problemas_digestivos", "tension_alta", "dolor_cabeza"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=13, column=0, columnspan=4)

    def create_input_fields(self):
        labels = ["Edad", "Sexo", "Bebidas por Semana", "Cervezas por Semana", "Bebidas de Fin de Semana",
                  "Bebidas Destiladas por Semana", "Vinos por Semana", "Pérdidas de Control",
                  "Diversión Dependencia Alcohol", "Problemas Digestivos", "Tensión Alta", "Dolor de Cabeza"]
        self.entries = []
        for i, label in enumerate(labels):
            tk.Label(self, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

    def agregar_encuesta(self):
        try:
            data = [entry.get() for entry in self.entries]
            agregar_encuesta(*data)
            messagebox.showinfo("Éxito", "Encuesta añadida correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar encuesta: {e}")

    def ver_encuestas(self):
        try:
            rows = obtener_encuestas()
            print(f"Fetched rows: {rows}")  # Debug print
            for row in self.tree.get_children():
                self.tree.delete(row)
            for row in rows:
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener encuestas: {e}")

    def actualizar_encuesta(self):
        try:
            selected_item = self.tree.selection()[0]
            data = [entry.get() for entry in self.entries]
            data.append(self.tree.item(selected_item)['values'][0])  # Add idEncuesta to the data
            actualizar_encuesta(*data)
            messagebox.showinfo("Éxito", "Encuesta actualizada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar encuesta: {e}")

    def eliminar_encuesta(self):
        try:
            selected_item = self.tree.selection()[0]
            id_encuesta = self.tree.item(selected_item)['values'][0]
            eliminar_encuesta(id_encuesta)
            self.tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar encuesta: {e}")