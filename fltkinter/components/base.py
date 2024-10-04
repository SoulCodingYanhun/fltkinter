import tkinter as tk
from ..colors import fluent_colors

class FluentWidget:
    def __init__(self, master, widget_class, **kwargs):
        self.master = master
        self.widget = widget_class(master, **kwargs)
        self.update_style()

    def update_style(self):
        pass

    def pack(self, **kwargs):
        self.widget.pack(**kwargs)

    def grid(self, **kwargs):
        self.widget.grid(**kwargs)

    def place(self, **kwargs):
        self.widget.place(**kwargs)