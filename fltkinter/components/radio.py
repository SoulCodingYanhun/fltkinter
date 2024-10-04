import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentRadio(FluentWidget):
    def __init__(self, master=None, variable=None, **kwargs):
        super().__init__(master, tk.Radiobutton, **kwargs)
        self.widget.configure(variable=variable)

    def update_style(self):
        self.widget.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            activebackground=fluent_colors.BACKGROUND,
            activeforeground=fluent_colors.PRIMARY,
            selectcolor=fluent_colors.PRIMARY,
            font=("Segoe UI", 10)
        )