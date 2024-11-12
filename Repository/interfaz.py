import tkinter as tk
from tkinter import ttk, messagebox
from .crud_operations import agregar_encuesta, obtener_encuestas, actualizar_encuesta, eliminar_encuesta
from .exportar_a_excel import exportar_a_excel
from Styles.styles import apply_styles

class AppEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Encuestas")
        self.geometry("1400x800")
        self.configure(bg="lightblue")

        # Apply styles
        apply_styles(self)

        # Campos de entrada para la encuesta
        self.create_input_fields()

        # Botones de acciones
        button_frame = ttk.Frame(self)
        button_frame.grid(row=12, column=0, columnspan=2, pady=10)
        ttk.Button(button_frame, text="Agregar Encuesta", command=self.agregar_encuesta, style="TButton").grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Ver Encuestas", command=self.ver_encuestas, style="TButton").grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Actualizar Encuesta", command=self.actualizar_encuesta, style="TButton").grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Eliminar Encuesta", command=self.eliminar_encuesta, style="TButton").grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="Exportar a Excel", command=self.exportar_a_excel, style="TButton").grid(row=0, column=4, padx=5)

        # Frame for the table
        frame = ttk.Frame(self)
        frame.grid(row=13, column=0, columnspan=2, sticky='nsew', padx=20)

        # Tabla para mostrar los registros
        self.tree = ttk.Treeview(frame, columns=(
            "idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "bebidas_fin_semana",
            "bebidas_destiladas_semana", "vinos_semana", "perdidas_control", "diversion_dependencia_alcohol",
            "problemas_digestivos", "tension_alta", "dolor_cabeza"), show="headings")

        # Set column headings and widths
        column_widths = {
            "idEncuesta": 50, "edad": 50, "sexo": 80, "bebidas_semana": 100, "cervezas_semana": 100,
            "bebidas_fin_semana": 100, "bebidas_destiladas_semana": 120, "vinos_semana": 100,
            "perdidas_control": 100, "diversion_dependencia_alcohol": 120, "problemas_digestivos": 120,
            "tension_alta": 120, "dolor_cabeza": 120
        }

        for col, width in column_widths.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=tk.CENTER)

        self.tree.grid(row=0, column=0, sticky='nsew')

        # Bind the select event
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Fetch and display data on startup
        self.ver_encuestas()

    def create_input_fields(self):
        labels = ["Edad", "Sexo", "Bebidas por Semana", "Cervezas por Semana", "Bebidas de Fin de Semana",
                  "Bebidas Destiladas por Semana", "Vinos por Semana", "Pérdidas de Control",
                  "Diversión Dependencia Alcohol", "Problemas Digestivos", "Tensión Alta", "Dolor de Cabeza"]
        self.entries = []
        input_frame = ttk.Frame(self)
        input_frame.grid(row=0, column=0, columnspan=2, pady=10)
        for i, label in enumerate(labels):
            ttk.Label(input_frame, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)
            if label == "Sexo":
                entry = ttk.Combobox(input_frame, values=["Hombre", "Mujer"])
            elif label in ["Diversión Dependencia Alcohol", "Problemas Digestivos"]:
                entry = ttk.Combobox(input_frame, values=["Sí", "No"])
            elif label == "Dolor de Cabeza":
                entry = ttk.Combobox(input_frame, values=["Alguna vez", "Muy a menudo", "Nunca"])
            elif label == "Tensión Alta":
                entry = ttk.Combobox(input_frame, values=["No lo se", "Sí", "No"])
            else:
                entry = ttk.Entry(input_frame)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.tree.item(selected_item, 'values')
            for entry, value in zip(self.entries, values[1:]):  # Skip idEncuesta
                if isinstance(entry, ttk.Combobox):
                    entry.set(value)
                else:
                    entry.delete(0, tk.END)
                    entry.insert(0, value)

    def agregar_encuesta(self):
        try:
            data = [entry.get() for entry in self.entries]
            agregar_encuesta(*data)
            messagebox.showinfo("Éxito", "Encuesta añadida correctamente.")
            self.ver_encuestas()  # Refresh the table
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar encuesta: {e}")

    def ver_encuestas(self):
        try:
            rows = obtener_encuestas()
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
            self.ver_encuestas()  # Refresh the table
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar encuesta: {e}")

    def eliminar_encuesta(self):
        try:
            selected_item = self.tree.selection()[0]
            id_encuesta = self.tree.item(selected_item)['values'][0]
            eliminar_encuesta(id_encuesta)
            self.tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
            self.ver_encuestas()  # Refresh the table
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar encuesta: {e}")

    def exportar_a_excel(self):
        try:
            exportar_a_excel()
            messagebox.showinfo("Éxito", "Datos exportados a encuestas.xlsx correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar datos: {e}")

if __name__ == "__main__":
    app = AppEncuestas()
    app.mainloop()