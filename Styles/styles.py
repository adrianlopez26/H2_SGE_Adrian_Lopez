import tkinter as tk
from tkinter import ttk

class CustomButton(tk.Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        # Configurar el botón con estilo personalizado
        self.configure(font=("Helvetica", 12), bg="#f0f0f0", fg="#333333", relief="flat", padx=10, pady=5)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.default_bg = "#f0f0f0"
        self.hover_bg = "#e0e0e0"

    def on_enter(self, event):
        # Cambiar el color de fondo al pasar el ratón
        self.configure(bg=self.hover_bg)

    def on_leave(self, event):
        # Restaurar el color de fondo al salir el ratón
        self.configure(bg=self.default_bg)

def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")

    # Configurar estilos para diferentes widgets
    style.configure("TLabel", font=("Helvetica", 12), background="lightblue", foreground="#333333")
    style.configure("TFrame", background="lightblue")
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), foreground="#ffffff", background="#333333")
    style.configure("Treeview", font=("Helvetica", 12), rowheight=25, fieldbackground="#f9f9f9", background="#f9f9f9")
    style.configure("TEntry", font=("Helvetica", 12), padding=5, relief="flat", background="#f0f0f0", foreground="#333333")
    style.configure("TCombobox", font=("Helvetica", 12), padding=5, relief="flat", background="#f0f0f0", foreground="#333333", arrowcolor="#333333")

    return CustomButton