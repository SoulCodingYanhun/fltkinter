import tkinter as tk
from .base import FluentWidget
from .button import FluentButton
from ..colors import fluent_colors

class FluentDialog(FluentWidget):
    def __init__(self, master=None, title="Dialog", message="", **kwargs):
        super().__init__(master, tk.Toplevel, **kwargs)
        self.title = title
        self.message = message
        self.result = None
        self.create_dialog()

    def create_dialog(self):
        self.widget.title(self.title)
        self.widget.geometry("300x150")
        self.widget.configure(bg=fluent_colors.BACKGROUND)

        label = tk.Label(self.widget, text=self.message, bg=fluent_colors.BACKGROUND, fg=fluent_colors.TEXT)
        label.pack(pady=20)

        button_frame = tk.Frame(self.widget, bg=fluent_colors.BACKGROUND)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        ok_button = FluentButton(button_frame, text="OK", command=self.on_ok)
        ok_button.pack(side=tk.LEFT, padx=5)

        cancel_button = FluentButton(button_frame, text="Cancel", command=self.on_cancel)
        cancel_button.pack(side=tk.LEFT, padx=5)

    def on_ok(self):
        self.result = True
        self.widget.destroy()

    def on_cancel(self):
        self.result = False
        self.widget.destroy()

    def show(self):
        self.widget.grab_set()
        self.widget.wait_window()
        return self.result