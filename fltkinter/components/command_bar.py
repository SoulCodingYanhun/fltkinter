import tkinter as tk
from .base import FluentWidget
from .button import FluentButton
from ..colors import fluent_colors

class FluentCommandBar(FluentWidget):
    def __init__(self, master=None, commands=None, **kwargs):
        super().__init__(master, tk.Frame, **kwargs)
        self.commands = commands or []
        self.create_command_bar()

    def create_command_bar(self):
        for command in self.commands:
            btn = FluentButton(self.widget, text=command['label'], command=command['action'])
            btn.pack(side=tk.LEFT, padx=2)

    def update_style(self):
        self.widget.configure(bg=fluent_colors.BACKGROUND)
        for child in self.widget.winfo_children():
            if isinstance(child, FluentButton):
                child.update_style()