import tkinter as tk
from tkinter import ttk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentSlider(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, ttk.Scale, **kwargs)

    def update_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Fluent.Horizontal.TScale',
                        troughcolor=fluent_colors.BACKGROUND,
                        slidercolor=fluent_colors.PRIMARY,
                        background=fluent_colors.BACKGROUND)
        self.widget.configure(style='Fluent.Horizontal.TScale')