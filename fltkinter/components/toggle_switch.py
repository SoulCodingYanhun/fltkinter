import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentToggleSwitch(FluentWidget):
    def __init__(self, master=None, command=None, **kwargs):
        super().__init__(master, tk.Canvas, width=60, height=30, **kwargs)
        self.command = command
        self.switched_on = False
        self.widget.bind("<Button-1>", self.toggle)

    def update_style(self):
        self.draw()

    def draw(self):
        self.widget.delete("all")
        if self.switched_on:
            self.widget.create_rectangle(0, 0, 60, 30, fill=fluent_colors.PRIMARY, outline="")
            self.widget.create_oval(30, 0, 60, 30, fill=fluent_colors.BACKGROUND, outline="")
        else:
            self.widget.create_rectangle(0, 0, 60, 30, fill=fluent_colors.DISABLED, outline="")
            self.widget.create_oval(0, 0, 30, 30, fill=fluent_colors.BACKGROUND, outline="")

    def toggle(self, event=None):
        self.switched_on = not self.switched_on
        self.draw()
        if self.command:
            self.command()