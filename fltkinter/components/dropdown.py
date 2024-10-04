import tkinter as tk
from tkinter import ttk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentDropdown(FluentWidget):
    def __init__(self, master=None, values=None, **kwargs):
        super().__init__(master, ttk.Combobox, values=values, **kwargs)
        self.widget.bind("<<ComboboxSelected>>", self.on_select)

    def update_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Fluent.TCombobox',
                        fieldbackground=fluent_colors.BACKGROUND,
                        background=fluent_colors.PRIMARY,
                        foreground=fluent_colors.TEXT,
                        arrowcolor=fluent_colors.PRIMARY)
        style.map('Fluent.TCombobox',
                  fieldbackground=[('readonly', fluent_colors.BACKGROUND)],
                  selectbackground=[('readonly', fluent_colors.PRIMARY)],
                  selectforeground=[('readonly', fluent_colors.BACKGROUND)])
        self.widget.configure(style='Fluent.TCombobox')

    def on_select(self, event):
        selected = self.widget.get()
        print(f"Selected: {selected}")
        return selected

    def set(self, value):
        self.widget.set(value)

    def get(self):
        return self.widget.get()