import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager

class FluentButton(FluentWidget):
    """
    A Fluent UI styled button widget.

    This class creates a button with Fluent UI styling, including hover and click effects.

    Attributes:
        widget (tk.Button): The underlying Tkinter Button widget.

    Methods:
        update_style(): Updates the button's style based on the current theme.
        disable(): Disables the button.
        enable(): Enables the button.
    """

    def __init__(self, master=None, **kwargs):
        """
        Initialize a FluentButton.

        Args:
            master: The parent widget.
            **kwargs: Additional keyword arguments to pass to the underlying Button widget.
        """
        super().__init__(master, tk.Button, **kwargs)
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<Button-1>", self.on_click)
        self.widget.bind("<ButtonRelease-1>", self.on_release)
        theme_manager.register_observer(self)

    def update_style(self):
        """Update the button's style based on the current theme."""
        self.widget.configure(
            bg=theme_manager.colors.PRIMARY,
            fg=theme_manager.colors.BACKGROUND,
            activebackground=theme_manager.colors.SECONDARY,
            activeforeground=theme_manager.colors.BACKGROUND,
            relief=tk.FLAT,
            padx=10,
            pady=5,
            font=("Segoe UI", 10),
            cursor="hand2"
        )

    def on_enter(self, e):
        self.widget['background'] = theme_manager.colors.SECONDARY

    def on_leave(self, e):
        self.widget['background'] = theme_manager.colors.PRIMARY

    def on_click(self, e):
        self.widget['relief'] = tk.SUNKEN

    def on_release(self, e):
        self.widget['relief'] = tk.FLAT

    def disable(self):
        self.widget.configure(state=tk.DISABLED, bg=theme_manager.colors.DISABLED)

    def enable(self):
        self.widget.configure(state=tk.NORMAL)
        self.update_style()