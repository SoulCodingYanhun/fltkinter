import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager
from ..utils import create_round_rectangle, animate
from ..acrylic import AcrylicFrame

class FluentTextField(FluentWidget):
    def __init__(self, master=None, placeholder="", **kwargs):
        self.acrylic_frame = AcrylicFrame(master, theme_manager.colors.BACKGROUND)
        super().__init__(self.acrylic_frame, tk.Canvas, **kwargs)
        self.placeholder = placeholder
        self.text = ""
        self.create_text_field()
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Key>", self.on_key)
        theme_manager.register_observer(self)

    def create_text_field(self):
        self.widget.config(width=200, height=40, bg='systemtransparent')
        self.shape = create_round_rectangle(self.widget, 10, 10, 190, 30, radius=10, fill='', outline=theme_manager.colors.PRIMARY)
        self.text_item = self.widget.create_text(20, 20, text=self.placeholder, fill=theme_manager.colors.DISABLED, anchor='w')
        self.widget.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        self.acrylic_frame.bg_color = theme_manager.colors.BACKGROUND
        self.acrylic_frame.on_resize(None)
        self.widget.itemconfig(self.shape, outline=theme_manager.colors.PRIMARY)
        if self.text:
            self.widget.itemconfig(self.text_item, fill=theme_manager.colors.TEXT)
        else:
            self.widget.itemconfig(self.text_item, fill=theme_manager.colors.DISABLED)

    def on_focus_in(self, event):
        if not self.text:
            self.widget.itemconfig(self.text_item, text="")
        animate(self.widget, 'highlightthickness', 1, 2, duration=200)

    def on_focus_out(self, event):
        if not self.text:
            self.widget.itemconfig(self.text_item, text=self.placeholder, fill=theme_manager.colors.DISABLED)
        animate(self.widget, 'highlightthickness', 2, 1, duration=200)

    def on_key(self, event):
        if event.char:
            self.text += event.char
        elif event.keysym == 'BackSpace':
            self.text = self.text[:-1]
        self.widget.itemconfig(self.text_item, text=self.text, fill=theme_manager.colors.TEXT)

    def get(self):
        return self.text

    def set(self, value):
        self.text = value
        self.widget.itemconfig(self.text_item, text=self.text, fill=theme_manager.colors.TEXT)

    def pack(self, **kwargs):
        self.acrylic_frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.acrylic_frame.grid(**kwargs)

    def place(self, **kwargs):
        self.acrylic_frame.place(**kwargs)