import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentSpinner(FluentWidget):
    def __init__(self, master=None, size=20, **kwargs):
        super().__init__(master, tk.Canvas, width=size, height=size, **kwargs)
        self.size = size
        self.angle = 0
        self.create_spinner()

    def create_spinner(self):
        self.widget.create_arc(0, 0, self.size, self.size, start=0, extent=60, fill=fluent_colors.PRIMARY)

    def update_style(self):
        self.widget.configure(bg=fluent_colors.BACKGROUND)
        self.widget.itemconfigure(1, fill=fluent_colors.PRIMARY)

    def start(self):
        self.spin()

    def spin(self):
        self.angle = (self.angle + 10) % 360
        self.widget.delete("all")
        self.widget.create_arc(0, 0, self.size, self.size, start=self.angle, extent=60, fill=fluent_colors.PRIMARY)
        self.widget.after(50, self.spin)