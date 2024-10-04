import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentEntry(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, tk.Entry, **kwargs)

    def update_style(self):
        self.widget.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            insertbackground=fluent_colors.TEXT,
            relief=tk.FLAT,
            bd=1,
            highlightthickness=1,
            highlightcolor=fluent_colors.PRIMARY,
            font=("Segoe UI", 10)
        )