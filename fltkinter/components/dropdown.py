import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager
from ..utils import create_round_rectangle, animate
from ..acrylic import AcrylicFrame

class FluentDropdown(FluentWidget):
    def __init__(self, master=None, values=None, **kwargs):
        self.acrylic_frame = AcrylicFrame(master, theme_manager.colors.BACKGROUND)
        super().__init__(self.acrylic_frame, tk.Canvas, **kwargs)
        self.values = values or []
        self.current_value = tk.StringVar()
        self.create_dropdown()
        self.bind("<Button-1>", self.show_options)
        theme_manager.register_observer(self)

    def create_dropdown(self):
        self.widget.config(width=200, height=30, bg='systemtransparent')
        self.shape = create_round_rectangle(self.widget, 5, 5, 195, 25, radius=5, fill='', outline=theme_manager.colors.PRIMARY)
        self.text = self.widget.create_text(15, 15, text="Select an option", anchor='w', fill=theme_manager.colors.TEXT)
        self.arrow = self.widget.create_polygon(180, 12, 185, 18, 190, 12, fill=theme_manager.colors.PRIMARY)
        self.widget.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        self.acrylic_frame.bg_color = theme_manager.colors.BACKGROUND
        self.acrylic_frame.on_resize(None)
        self.widget.itemconfig(self.shape, outline=theme_manager.colors.PRIMARY)
        self.widget.itemconfig(self.text, fill=theme_manager.colors.TEXT)
        self.widget.itemconfig(self.arrow, fill=theme_manager.colors.PRIMARY)

    def show_options(self, event):
        menu = tk.Menu(self.widget, tearoff=0)
        for value in self.values:
            menu.add_command(label=value, command=lambda v=value: self.select_option(v))
        
        def post_menu():
            menu.post(event.x_root, event.y_root)
        
        animate(self.widget, 'arrow_rotation', 0, 180, duration=200, update_func=self.rotate_arrow)
        self.widget.after(200, post_menu)

    def rotate_arrow(self, angle):
        self.widget.delete(self.arrow)
        self.arrow = self.widget.create_polygon(
            180, 12, 185, 18, 190, 12, 
            fill=theme_manager.colors.PRIMARY,
            tags='arrow'
        )
        self.widget.rotate(self.arrow, 185, 15, angle)

    def select_option(self, value):
        self.current_value.set(value)
        self.widget.itemconfig(self.text, text=value)

    def get(self):
        return self.current_value.get()

    def set(self, value):
        if value in self.values:
            self.current_value.set(value)
            self.widget.itemconfig(self.text, text=value)

    def pack(self, **kwargs):
        self.acrylic_frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.acrylic_frame.grid(**kwargs)

    def place(self, **kwargs):
        self.acrylic_frame.place(**kwargs)