import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentPanel(FluentWidget):
    def __init__(self, master=None, side=tk.LEFT, width=200, **kwargs):
        super().__init__(master, tk.Frame, **kwargs)
        self.side = side
        self.width = width
        self.is_open = False
        self.create_panel()

    def create_panel(self):
        self.widget.configure(width=self.width, bg=fluent_colors.BACKGROUND)
        self.widget.pack_propagate(False)
        self.close_button = tk.Button(self.widget, text="×", command=self.toggle)
        self.close_button.pack(anchor=tk.NE, padx=5, pady=5)

    def update_style(self):
        self.widget.configure(bg=fluent_colors.BACKGROUND)
        self.close_button.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            activebackground=fluent_colors.PRIMARY,
            activeforeground=fluent_colors.BACKGROUND,
            relief=tk.FLAT,
            font=("Segoe UI", 12, "bold")
        )

    def toggle(self):
        if self.is_open:
            self.widget.pack_forget()
        else:
            self.widget.pack(side=self.side, fill=tk.Y)
        self.is_open = not self.is_open