import tkinter as tk

class FluentLayout:
    @staticmethod
    def grid(widget, row, column, padx=5, pady=5, **kwargs):
        widget.widget.grid(row=row, column=column, padx=padx, pady=pady, **kwargs)

    @staticmethod
    def pack(widget, side=tk.TOP, fill=tk.NONE, expand=False, padx=5, pady=5, **kwargs):
        widget.widget.pack(side=side, fill=fill, expand=expand, padx=padx, pady=pady, **kwargs)

    @staticmethod
    def place(widget, x, y, **kwargs):
        widget.widget.place(x=x, y=y, **kwargs)