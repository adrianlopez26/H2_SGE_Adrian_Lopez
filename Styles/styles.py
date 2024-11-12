# styles/styles.py
import tkinter as tk
from tkinter import ttk


def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")  # Using a base modern theme

    # Modern button styles with gradient-like appearance
    style.configure("TButton",
                    font=("Segoe UI Variable", 15, "bold"),
                    foreground="white",
                    background="#1e40af",  # Deep blue for a professional look
                    padding=12,
                    borderwidth=0,
                    relief="flat")
    style.map("TButton",
              background=[("active", "#1d4ed8"), ("disabled", "#6b7280")],
              foreground=[("disabled", "#d1d5db")],
              relief=[("pressed", "solid")])

    # Label styles with accent colors for emphasis
    style.configure("TLabel",
                    font=("Segoe UI Variable", 14),
                    background="#f3f4f6",  # Neutral background color
                    foreground="#111827")  # Dark gray for contrast

    style.configure("TFrame", background="#f3f4f6")

    # Treeview header with modern color and typography
    style.configure("Treeview.Heading",
                    font=("Segoe UI Variable", 14, "bold"),
                    foreground="white",
                    background="#1e40af")

    style.configure("Treeview",
                    font=("Segoe UI", 12),
                    rowheight=30,
                    fieldbackground="#f9fafb",
                    background="#f9fafb",
                    borderwidth=0,
                    highlightthickness=0)

    # Modern Entry and Combobox styles with flat look
    style.configure("TEntry",
                    font=("Segoe UI", 12),
                    padding=10,
                    relief="flat",
                    borderwidth=1,
                    background="#f1f5f9",
                    foreground="#1f2937")  # Dark text
    style.map("TEntry",
              fieldbackground=[("focus", "#e2e8f0")],  # Lighter on focus
              bordercolor=[("focus", "#2563eb")])  # Blue outline on focus

    style.configure("TCombobox",
                    font=("Segoe UI", 12),
                    padding=10,
                    relief="flat",
                    borderwidth=1,
                    background="#f1f5f9",
                    foreground="#1f2937")
    style.map("TCombobox",
              fieldbackground=[("focus", "#e2e8f0")],
              bordercolor=[("focus", "#2563eb")])

    # Custom hover effects for buttons with smooth transition
    style.map("TButton",
              background=[("hover", "#2563eb"), ("!disabled", "#1e40af")],
              foreground=[("!disabled", "white")])

    # Scrollbar customization with thin, modern design
    style.configure("Vertical.TScrollbar",
                    gripcount=0,
                    background="#e5e7eb",
                    darkcolor="#e5e7eb",
                    lightcolor="#f3f4f6",
                    troughcolor="#d1d5db",
                    bordercolor="#d1d5db",
                    arrowcolor="#1e40af")  # Blue for arrows

    style.configure("Horizontal.TScrollbar",
                    gripcount=0,
                    background="#e5e7eb",
                    darkcolor="#e5e7eb",
                    lightcolor="#f3f4f6",
                    troughcolor="#d1d5db",
                    bordercolor="#d1d5db",
                    arrowcolor="#1e40af")
