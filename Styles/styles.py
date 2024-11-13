import tkinter as tk
from tkinter import ttk

class CustomButton(tk.Canvas):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.text = text
        self.configure(height=40, width=150, bg="lightblue", bd=0, highlightthickness=0)  # Set bg color
        self.text_id = self.create_text(75, 20, text=self.text, font=("Helvetica", 12, "bold"), fill="black", tags="text")  # Set text color
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<ButtonPress>", self.on_press)
        self.bind("<ButtonRelease>", self.on_release)
        self.hover_color = "#00FFFF"  # Electric blue
        self.default_color = "lightblue"  # Light blue background
        self.current_color = self.default_color

    def on_enter(self, event):
        self.animate_color_change(self.default_color, self.hover_color)

    def on_leave(self, event):
        self.animate_color_change(self.hover_color, self.default_color)

    def on_press(self, event):
        if self.command:
            self.command()

    def on_release(self, event):
        self.on_enter(event)

    def animate_color_change(self, start_color, end_color):
        start_rgb = self.winfo_rgb(start_color)
        end_rgb = self.winfo_rgb(end_color)
        r_diff = (end_rgb[0] - start_rgb[0]) // 10
        g_diff = (end_rgb[1] - start_rgb[1]) // 10
        b_diff = (end_rgb[2] - start_rgb[2]) // 10

        for i in range(11):
            new_color = f"#{max(0, min((start_rgb[0] + (r_diff * i)) // 256, 255)):02x}{max(0, min((start_rgb[1] + (g_diff * i)) // 256, 255)):02x}{max(0, min((start_rgb[2] + (b_diff * i)) // 256, 255)):02x}"
            self.after(i * 50, lambda color=new_color, step=i: self.create_gradient(color, step))

    def create_gradient(self, color, step):
        width = self.winfo_width()
        step_width = width // 10
        self.delete("gradient")
        for i in range(step + 1):
            self.create_rectangle(i * step_width, 0, (i + 1) * step_width, 40, fill=color, outline="", tags="gradient")
        self.tag_lower("gradient", self.text_id)

def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")  # Use a modern theme

    # Responsive styles for labels
    style.configure("TLabel",
                    font=("Segoe UI Variable", 14),
                    background="#f3f4f6",  # Neutral background color
                    foreground="#111827")  # Dark gray for contrast

    # Responsive background for frames
    style.configure("TFrame", background="#f3f4f6")

    # Modern Treeview header with prominent typography
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

    # Clean and modern styles for Entry and Combobox
    style.configure("TEntry",
                    font=("Segoe UI", 12),
                    padding=10,
                    relief="flat",
                    borderwidth=1,
                    background="#f1f5f9",
                    foreground="#1f2937")  # Dark text
    style.map("TEntry",
              fieldbackground=[("focus", "#e2e8f0")],
              bordercolor=[("focus", "#2563eb")])  # Blue highlight on focus

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

    # Custom Scrollbar with a sleek and modern design
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

    return CustomButton