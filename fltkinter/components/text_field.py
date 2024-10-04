import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentTextField(FluentWidget):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, tk.Entry, **kwargs)
        self.placeholder = placeholder
        self.widget.bind("<FocusIn>", self.on_focus_in)
        self.widget.bind("<FocusOut>", self.on_focus_out)
        self.show_placeholder()

    def update_style(self):
        self.widget.configure(
            bg=fluent_colors.BACKGROUND,
            fg=fluent_colors.TEXT,
            insertbackground=fluent_colors.TEXT,
            relief=tk.FLAT,
            bd=1,
            highlightthickness=1,
            highlightcolor=fluent_colors.PRIMARY,
            font=("Segoe UI", 10)
        )

    def on_focus_in(self, event):
        if self.widget.get() == self.placeholder:
            self.widget.delete(0, tk.END)
            self.widget.config(fg=fluent_colors.TEXT)

    def on_focus_out(self, event):
        if not self.widget.get():
            self.show_placeholder()

    def show_placeholder(self):
        self.widget.delete(0, tk.END)
        self.widget.insert(0, self.placeholder)
        self.widget.config(fg=fluent_colors.DISABLED)

    def get(self):
        value = self.widget.get()
        return "" if value == self.placeholder else value

    def set(self, value):
        self.widget.delete(0, tk.END)
        if value:
            self.widget.insert(0, value)
            self.widget.config(fg=fluent_colors.TEXT)
        else:
            self.show_placeholder()