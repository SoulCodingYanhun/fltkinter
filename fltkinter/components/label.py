import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentLabel(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, tk.Label, **kwargs)

    def update_style(self):
        self.widget.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            font=("Segoe UI", 10)
        )