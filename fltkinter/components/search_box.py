import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentSearchBox(FluentWidget):
    def __init__(self, master=None, placeholder="Search...", command=None, **kwargs):
        super().__init__(master, tk.Entry, **kwargs)
        self.placeholder = placeholder
        self.command = command
        self.create_search_box()

    def create_search_box(self):
        self.widget.insert(0, self.placeholder)
        self.widget.bind("<FocusIn>", self.on_focus_in)
        self.widget.bind("<FocusOut>", self.on_focus_out)
        self.widget.bind("<Return>", self.on_search)

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
            self.widget.insert(0, self.placeholder)
            self.widget.config(fg=fluent_colors.DISABLED)

    def on_search(self, event):
        if self.command:
            self.command(self.widget.get())