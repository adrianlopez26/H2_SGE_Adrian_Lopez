import tkinter as tk
from tkinter import ttk, messagebox
from .crud_operations import agregar_encuesta, obtener_encuestas, actualizar_encuesta, eliminar_encuesta
from .exportar_a_excel import exportar_a_excel
from Styles.styles import apply_styles
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppEncuestas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Encuestas")
        self.geometry("1600x900")
        self.configure(bg="lightblue")

        # Aplicar estilos
        CustomButton = apply_styles(self)

        # Crear un marco principal para centrar el contenido
        main_frame = ttk.Frame(self, style="TFrame")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Centrar el marco principal
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Campos de entrada para la encuesta
        self.create_input_fields(main_frame)

        # Botones de acciones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=12, column=0, columnspan=2, pady=10)
        CustomButton(button_frame, text="Agregar Encuesta", command=self.agregar_encuesta).grid(row=0, column=0, padx=5)
        CustomButton(button_frame, text="Ver Encuestas", command=self.ver_encuestas).grid(row=0, column=1, padx=5)
        CustomButton(button_frame, text="Actualizar Encuesta", command=self.actualizar_encuesta).grid(row=0, column=2, padx=5)
        CustomButton(button_frame, text="Eliminar Encuesta", command=self.eliminar_encuesta).grid(row=0, column=3, padx=5)
        CustomButton(button_frame, text="Exportar a Excel", command=self.exportar_a_excel).grid(row=0, column=4, padx=5)
        CustomButton(button_frame, text="Generar Gráfico", command=self.generar_grafico).grid(row=0, column=5, padx=5)

        # Marco para la tabla
        frame = ttk.Frame(main_frame)
        frame.grid(row=13, column=0, columnspan=2, sticky='nsew', padx=20)

        # Tabla para mostrar los registros
        self.tree = ttk.Treeview(frame, columns=(
            "idEncuesta", "edad", "sexo", "bebidas_semana", "cervezas_semana", "bebidas_fin_semana",
            "bebidas_destiladas_semana", "vinos_semana", "perdidas_control", "diversion_dependencia_alcohol",
            "problemas_digestivos", "tension_alta", "dolor_cabeza"), show="headings")

        # Establecer encabezados y anchos de columna
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

        # Vincular el evento de selección
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Obtener y mostrar datos al iniciar
        self.ver_encuestas()

    def create_input_fields(self, parent):
        labels = ["Edad", "Sexo", "Bebidas por Semana", "Cervezas por Semana", "Bebidas de Fin de Semana",
                  "Bebidas Destiladas por Semana", "Vinos por Semana", "Pérdidas de Control",
                  "Diversión Dependencia Alcohol", "Problemas Digestivos", "Tensión Alta", "Dolor de Cabeza"]
        self.entries = []
        input_frame = ttk.Frame(parent)
        input_frame.grid(row=0, column=0, columnspan=2, pady=10)
        for i, label in enumerate(labels):
            ttk.Label(input_frame, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)
            if label == "Sexo":
                entry = ttk.Combobox(input_frame, values=["Hombre", "Mujer"], state="readonly", width=20)
            elif label in ["Diversión Dependencia Alcohol", "Problemas Digestivos"]:
                entry = ttk.Combobox(input_frame, values=["Sí", "No"], state="readonly", width=20)
            elif label == "Dolor de Cabeza":
                entry = ttk.Combobox(input_frame, values=["Alguna vez", "Muy a menudo", "Nunca"], state="readonly",
                                     width=20)
            elif label == "Tensión Alta":
                entry = ttk.Combobox(input_frame, values=["No lo se", "Sí", "No"], state="readonly", width=20)
            else:
                entry = ttk.Entry(input_frame, width=23)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        # Añadir campos de filtro a la derecha de la tabla
        filter_frame = ttk.Frame(parent)
        filter_frame.grid(row=13, column=2, padx=10, pady=10, sticky='n')

        ttk.Label(filter_frame, text="Edad:").grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.age_filter = ttk.Entry(filter_frame, width=10)
        self.age_filter.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(filter_frame, text="Sexo:").grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.sex_filter = ttk.Combobox(filter_frame, values=["", "Hombre", "Mujer"], state="readonly", width=10)
        self.sex_filter.grid(row=1, column=1, padx=5, pady=2)

        # Añadir botones de filtro
        filter_button = ttk.Button(filter_frame, text="Aplicar", command=self.ver_encuestas)
        filter_button.grid(row=2, column=0, columnspan=2, pady=5)

        clear_filter_button = ttk.Button(filter_frame, text="Eliminar", command=self.clear_filters)
        clear_filter_button.grid(row=3, column=0, columnspan=2, pady=5)

    def clear_filters(self):
        # Limpiar los filtros
        self.age_filter.delete(0, tk.END)
        self.sex_filter.set("")
        self.ver_encuestas()

    def on_tree_select(self, event):
        # Manejar la selección de un elemento en la tabla
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.tree.item(selected_item, 'values')
            for entry, value in zip(self.entries, values[1:]):  # Omitir idEncuesta
                if isinstance(entry, ttk.Combobox):
                    entry.set(value)
                else:
                    entry.delete(0, tk.END)
                    entry.insert(0, value)

    def agregar_encuesta(self):
        try:
            # Obtener datos de los campos de entrada
            data = [entry.get() for entry in self.entries]
            agregar_encuesta(*data)
            messagebox.showinfo("Éxito", "Encuesta añadida correctamente.")
            self.ver_encuestas()  # Actualizar la tabla
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar encuesta: {e}")

    def ver_encuestas(self):
        try:
            # Obtener valores de los filtros
            age_filter = self.age_filter.get()
            sex_filter = self.sex_filter.get()

            # Obtener todas las filas
            rows = obtener_encuestas()

            # Aplicar filtros
            if age_filter:
                rows = [row for row in rows if str(row[1]) == age_filter]  # Suponiendo que la edad es la segunda columna
            if sex_filter:
                rows = [row for row in rows if row[2] == sex_filter]  # Suponiendo que el sexo es la tercera columna

            # Limpiar la tabla
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Insertar filas filtradas
            for row in rows:
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener encuestas: {e}")

    def actualizar_encuesta(self):
        try:
            # Obtener el elemento seleccionado
            selected_item = self.tree.selection()[0]
            data = [entry.get() for entry in self.entries]
            data.append(self.tree.item(selected_item)['values'][0])  # Añadir idEncuesta a los datos
            actualizar_encuesta(*data)
            messagebox.showinfo("Éxito", "Encuesta actualizada correctamente.")
            self.ver_encuestas()  # Actualizar la tabla
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar encuesta: {e}")

    def eliminar_encuesta(self):
        try:
            # Obtener el elemento seleccionado
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item)['values']
            id_encuesta = values[0]

            # Pedir confirmación
            confirm = messagebox.askyesno("Confirmar eliminación",
                                            f"¿Está seguro de que desea eliminar la encuesta con ID {id_encuesta}?")

            if confirm:
                eliminar_encuesta(id_encuesta)
                self.tree.delete(selected_item)
                messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
                self.ver_encuestas()  # Actualizar la tabla

                # Mostrar detalles de la encuesta eliminada en una nueva ventana
                details_window = tk.Toplevel(self)
                details_window.title("Detalles de la Encuesta Eliminada")
                details_window.geometry("400x300")

                details_text = "\n".join([f"{col}: {val}" for col, val in zip(self.tree['columns'], values)])
                tk.Label(details_window, text=details_text, justify=tk.LEFT, padx=10, pady=10).pack()

        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar encuesta: {e}")

    def exportar_a_excel(self):
        try:
            # Obtener datos de la tabla
            data = [self.tree.item(item)['values'] for item in self.tree.get_children()]

            if not data:
                messagebox.showinfo("Información", "No hay datos para exportar.")
                return

            # Llamar a la función de exportación
            exportar_a_excel(data)
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar datos: {e}")

    def generar_grafico(self):
        try:
            # Obtener datos filtrados de la tabla
            data = [self.tree.item(item)['values'] for item in self.tree.get_children()]

            if not data:
                messagebox.showinfo("Información", "No hay datos para generar el gráfico.")
                return

            # Extraer columnas relevantes para el gráfico
            edades = [row[1] for row in data]  # Suponiendo que la edad es la segunda columna
            sexos = [row[2] for row in data]  # Suponiendo que el sexo es la tercera columna

            # Crear una nueva ventana
            new_window = tk.Toplevel(self)
            new_window.title("Gráfico de Encuestas")
            new_window.geometry("800x600")

            # Crear una figura y un eje
            fig, ax = plt.subplots()

            # Graficar datos
            hombres = [edad for edad, sexo in zip(edades, sexos) if sexo == 'Hombre']
            mujeres = [edad for edad, sexo in zip(edades, sexos) if sexo == 'Mujer']

            if hombres or mujeres:
                ax.hist([hombres, mujeres], bins=range(min(edades), max(edades) + 1), alpha=0.7,
                        label=['Hombres', 'Mujeres'], color=['blue', 'pink'])
                ax.set_xlabel('Edad')
                ax.set_ylabel('Frecuencia')
                ax.set_title('Distribución de Edades por Sexo')
                ax.legend()
            else:
                messagebox.showinfo("Información", "No hay datos suficientes para generar el gráfico.")
                return

            # Incrustar el gráfico en la nueva ventana
            canvas = FigureCanvasTkAgg(fig, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", f"Error al generar gráfico: {e}")

if __name__ == "__main__":
    app = AppEncuestas()
    app.mainloop()