import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentCheckbox(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, tk.Checkbutton, **kwargs)
        self.var = tk.BooleanVar()
        self.widget.configure(variable=self.var)

    def update_style(self):
        self.widget.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            activebackground=fluent_colors.BACKGROUND,
            activeforeground=fluent_colors.PRIMARY,
            selectcolor=fluent_colors.PRIMARY,
            font=("Segoe UI", 10)
        )

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)