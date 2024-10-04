import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentChoiceGroup(FluentWidget):
    def __init__(self, master=None, choices=None, command=None, **kwargs):
        super().__init__(master, tk.Frame, **kwargs)
        self.choices = choices or []
        self.command = command
        self.var = tk.StringVar()
        self.radios = []
        self.create_radios()

    def create_radios(self):
        for choice in self.choices:
            radio = tk.Radiobutton(self.widget, text=choice, variable=self.var, value=choice,
                                   command=self.on_select)
            radio.pack(anchor=tk.W, pady=2)
            self.radios.append(radio)
        self.update_style()

    def update_style(self):
        self.widget.configure(bg=fluent_colors.BACKGROUND)
        for radio in self.radios:
            radio.configure(
                bg=fluent_colors.BACKGROUND,
                fg=fluent_colors.TEXT,
                activebackground=fluent_colors.BACKGROUND,
                activeforeground=fluent_colors.PRIMARY,
                selectcolor=fluent_colors.PRIMARY,
                font=("Segoe UI", 10)
            )

    def on_select(self):
        if self.command:
            self.command(self.var.get())