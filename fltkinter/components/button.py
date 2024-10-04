import tkinter as tk
from .base import FluentWidget
from ..theme_manager import theme_manager
from ..utils import create_round_rectangle, animate
from ..acrylic import AcrylicFrame

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
        self.acrylic_frame = AcrylicFrame(master, theme_manager.colors.PRIMARY)
        super().__init__(self.acrylic_frame, tk.Canvas, **kwargs)
        self.text = kwargs.get('text', '')
        self.command = kwargs.get('command', None)
        self.state = tk.NORMAL
        self.create_button()
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        theme_manager.register_observer(self)

    def create_button(self):
        self.widget.config(width=120, height=40, bg='systemtransparent')
        self.shape = create_round_rectangle(self.widget, 10, 10, 110, 30, radius=10, fill='')
        self.text_item = self.widget.create_text(60, 20, text=self.text, fill=theme_manager.colors.BACKGROUND)
        self.widget.pack(fill=tk.BOTH, expand=True)

    def update_style(self):
        """Update the button's style based on the current theme."""
        self.acrylic_frame.bg_color = theme_manager.colors.PRIMARY
        self.acrylic_frame.on_resize(None)
        self.widget.itemconfig(self.text_item, fill=theme_manager.colors.BACKGROUND)

    def on_enter(self, e):
        if self.state == tk.NORMAL:
            animate(self.acrylic_frame, 'bg_color', 
                    self.acrylic_frame.bg_color, 
                    theme_manager.colors.SECONDARY, 
                    duration=200, 
                    update_func=self.acrylic_frame.on_resize)

    def on_leave(self, e):
        if self.state == tk.NORMAL:
            animate(self.acrylic_frame, 'bg_color', 
                    self.acrylic_frame.bg_color, 
                    theme_manager.colors.PRIMARY, 
                    duration=200, 
                    update_func=self.acrylic_frame.on_resize)

    def on_click(self, e):
        if self.state == tk.NORMAL:
            self.acrylic_frame.bg_color = theme_manager.colors.PRIMARY
            self.acrylic_frame.on_resize(None)

    def on_release(self, e):
        if self.state == tk.NORMAL:
            self.acrylic_frame.bg_color = theme_manager.colors.SECONDARY
            self.acrylic_frame.on_resize(None)
            if self.command:
                self.command()

    def disable(self):
        self.state = tk.DISABLED
        self.acrylic_frame.bg_color = theme_manager.colors.DISABLED
        self.acrylic_frame.on_resize(None)

    def enable(self):
        self.state = tk.NORMAL
        self.update_style()

    def pack(self, **kwargs):
        self.acrylic_frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.acrylic_frame.grid(**kwargs)

    def place(self, **kwargs):
        self.acrylic_frame.place(**kwargs)