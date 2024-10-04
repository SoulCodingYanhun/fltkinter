import tkinter as tk
from tkinter import ttk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentComboBox(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, ttk.Combobox, **kwargs)

    def update_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TCombobox',
                        fieldbackground=fluent_colors.BACKGROUND,
                        background=fluent_colors.PRIMARY,
                        foreground=fluent_colors.TEXT,
                        arrowcolor=fluent_colors.PRIMARY)
        style.map('TCombobox',
                  fieldbackground=[('readonly', fluent_colors.BACKGROUND)],
                  selectbackground=[('readonly', fluent_colors.PRIMARY)],
                  selectforeground=[('readonly', fluent_colors.BACKGROUND)])
        self.widget.configure(style='TCombobox')