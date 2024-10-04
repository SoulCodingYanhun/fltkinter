import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager
from ..utils import create_round_rectangle, animate
from ..acrylic import AcrylicFrame

class FluentRadio(FluentWidget):
    def __init__(self, master=None, variable=None, value=None, **kwargs):
        self.acrylic_frame = AcrylicFrame(master, theme_manager.colors.BACKGROUND)
        super().__init__(self.acrylic_frame, tk.Canvas, **kwargs)
        self.text = kwargs.get('text', '')
        self.variable = variable
        self.value = value
        self.create_radio()
        self.bind("<Button-1>", self.select)
        theme_manager.register_observer(self)

    def create_radio(self):
        self.widget.config(width=200, height=30, bg='systemtransparent')
        self.outer_circle = self.widget.create_oval(5, 5, 25, 25, outline=theme_manager.colors.PRIMARY)
        self.inner_circle = self.widget.create_oval(10, 10, 20, 20, fill=theme_manager.colors.PRIMARY, state='hidden')
        self.label = self.widget.create_text(35, 15, text=self.text, anchor='w', fill=theme_manager.colors.TEXT)
        self.widget.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        self.acrylic_frame.bg_color = theme_manager.colors.BACKGROUND
        self.acrylic_frame.on_resize(None)
        self.widget.itemconfig(self.outer_circle, outline=theme_manager.colors.PRIMARY)
        self.widget.itemconfig(self.inner_circle, fill=theme_manager.colors.PRIMARY)
        self.widget.itemconfig(self.label, fill=theme_manager.colors.TEXT)

    def select(self, event):
        self.variable.set(self.value)
        animate(self.widget, 'inner_circle_radius', 0, 5, duration=200, update_func=self.update_inner_circle)

    def update_inner_circle(self, radius):
        self.widget.coords(self.inner_circle, 15-radius, 15-radius, 15+radius, 15+radius)
        self.widget.itemconfig(self.inner_circle, state='normal')

    def pack(self, **kwargs):
        self.acrylic_frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.acrylic_frame.grid(**kwargs)

    def place(self, **kwargs):
        self.acrylic_frame.place(**kwargs)