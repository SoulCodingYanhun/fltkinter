import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager
from ..utils import create_round_rectangle, animate
from ..acrylic import AcrylicFrame

class FluentCheckbox(FluentWidget):
    def __init__(self, master=None, **kwargs):
        self.acrylic_frame = AcrylicFrame(master, theme_manager.colors.BACKGROUND)
        super().__init__(self.acrylic_frame, tk.Canvas, **kwargs)
        self.text = kwargs.get('text', '')
        self.var = tk.BooleanVar()
        self.create_checkbox()
        self.bind("<Button-1>", self.toggle)
        theme_manager.register_observer(self)

    def create_checkbox(self):
        self.widget.config(width=200, height=30, bg='systemtransparent')
        self.box = create_round_rectangle(self.widget, 5, 5, 25, 25, radius=5, outline=theme_manager.colors.PRIMARY)
        self.check = self.widget.create_line(10, 15, 15, 20, 20, 10, fill=theme_manager.colors.PRIMARY, width=2, state='hidden')
        self.label = self.widget.create_text(35, 15, text=self.text, anchor='w', fill=theme_manager.colors.TEXT)
        self.widget.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        self.acrylic_frame.bg_color = theme_manager.colors.BACKGROUND
        self.acrylic_frame.on_resize(None)
        self.widget.itemconfig(self.box, outline=theme_manager.colors.PRIMARY)
        self.widget.itemconfig(self.check, fill=theme_manager.colors.PRIMARY)
        self.widget.itemconfig(self.label, fill=theme_manager.colors.TEXT)

    def toggle(self, event):
        self.var.set(not self.var.get())
        if self.var.get():
            animate(self.widget, 'check_opacity', 0, 1, duration=200, update_func=self.update_check_opacity)
        else:
            animate(self.widget, 'check_opacity', 1, 0, duration=200, update_func=self.update_check_opacity)

    def update_check_opacity(self, opacity):
        self.widget.itemconfig(self.check, state='normal', fill=theme_manager.colors.PRIMARY + hex(int(opacity * 255))[2:].zfill(2))

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)
        self.update_check()

    def pack(self, **kwargs):
        self.acrylic_frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.acrylic_frame.grid(**kwargs)

    def place(self, **kwargs):
        self.acrylic_frame.place(**kwargs)