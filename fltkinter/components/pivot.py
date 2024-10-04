import tkinter as tk
from .base import FluentWidget
from ..colors import fluent_colors

class FluentPivot(FluentWidget):
    def __init__(self, master=None, tabs=None, **kwargs):
        super().__init__(master, tk.Frame, **kwargs)
        self.tabs = tabs or []
        self.current_tab = None
        self.create_pivot()

    def create_pivot(self):
        self.tab_frame = tk.Frame(self.widget, bg=fluent_colors.BACKGROUND)
        self.tab_frame.pack(fill=tk.X)

        self.content_frame = tk.Frame(self.widget, bg=fluent_colors.BACKGROUND)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        for tab in self.tabs:
            btn = tk.Button(self.tab_frame, text=tab['label'], command=lambda t=tab: self.show_tab(t))
            btn.pack(side=tk.LEFT, padx=2)

        if self.tabs:
            self.show_tab(self.tabs[0])

    def show_tab(self, tab):
        if self.current_tab:
            self.current_tab.pack_forget()

        self.current_tab = tab['content'](self.content_frame)
        self.current_tab.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        self.widget.configure(bg=fluent_colors.BACKGROUND)
        self.tab_frame.configure(bg=fluent_colors.BACKGROUND)
        self.content_frame.configure(bg=fluent_colors.BACKGROUND)
        for child in self.tab_frame.winfo_children():
            child.configure(
                bg=fluent_colors.PRIMARY,
                fg=fluent_colors.BACKGROUND,
                activebackground=fluent_colors.SECONDARY,
                activeforeground=fluent_colors.BACKGROUND
            )