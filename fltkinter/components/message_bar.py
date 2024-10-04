import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentMessageBar(FluentWidget):
    def __init__(self, master=None, message="", message_type="info", **kwargs):
        super().__init__(master, tk.Frame, **kwargs)
        self.message = message
        self.message_type = message_type
        self.create_message_bar()

    def create_message_bar(self):
        self.label = tk.Label(self.widget, text=self.message, anchor=tk.W)
        self.label.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)
        self.close_button = tk.Button(self.widget, text="×", command=self.hide)
        self.close_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.update_style()

    def update_style(self):
        bg_color = fluent_colors.PRIMARY if self.message_type == "info" else fluent_colors.DISABLED
        self.widget.configure(bg=bg_color)
        self.label.configure(
            bg=bg_color,
            fg=fluent_colors.BACKGROUND,
            font=("Segoe UI", 10)
        )
        self.close_button.configure(
            bg=bg_color,
            fg=fluent_colors.BACKGROUND,
            activebackground=fluent_colors.SECONDARY,
            activeforeground=fluent_colors.BACKGROUND,
            relief=tk.FLAT,
            font=("Segoe UI", 12, "bold")
        )

    def show(self, message=None, message_type=None):
        if message:
            self.message = message
            self.label.configure(text=self.message)
        if message_type:
            self.message_type = message_type
        self.update_style()
        self.widget.pack(fill=tk.X, padx=10, pady=5)

    def hide(self):
        self.widget.pack_forget()