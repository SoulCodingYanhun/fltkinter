import tkinter as tk
from tkinter import ttk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentProgressBar(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, ttk.Progressbar, **kwargs)

    def update_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Fluent.Horizontal.TProgressbar',
                        troughcolor=fluent_colors.BACKGROUND,
                        background=fluent_colors.PRIMARY,
                        thickness=6)
        self.widget.configure(style='Fluent.Horizontal.TProgressbar')