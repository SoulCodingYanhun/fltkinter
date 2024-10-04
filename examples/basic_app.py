import tkinter as tk
from fltkinter import (
    FluentButton, FluentTextField, FluentCheckbox, FluentRadio, FluentLabel,
    FluentDropdown, FluentProgressBar, FluentSlider, FluentToggleSwitch,
    FluentChoiceGroup, FluentPanel, FluentMessageBar, FluentCommandBar,
    FluentDialog, FluentPivot, FluentSearchBox, FluentSpinner,
    set_theme, fluent_colors
)

class BasicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fluent UI Example")
        self.geometry("800x600")
        self.configure(bg=fluent_colors.BACKGROUND)

        self.create_widgets()

    def create_widgets(self):
        self.label = FluentLabel(self, text="Welcome to Fluent UI!")
        self.label.pack(pady=10)

        self.text_field = FluentTextField(self, placeholder="Enter text here...")
        self.text_field.pack(pady=5)

        self.button = FluentButton(self, text="Click me!", command=self.on_button_click)
        self.button.pack(pady=5)

        self.checkbox = FluentCheckbox(self, text="Check me")
        self.checkbox.pack(pady=5)

        self.radio_var = tk.StringVar(value="1")
        self.radio1 = FluentRadio(self, text="Option 1", variable=self.radio_var, value="1")
        self.radio1.pack(pady=2)
        self.radio2 = FluentRadio(self, text="Option 2", variable=self.radio_var, value="2")
        self.radio2.pack(pady=2)

        self.dropdown = FluentDropdown(self, values=["Item 1", "Item 2", "Item 3"])
        self.dropdown.pack(pady=5)

        self.progressbar = FluentProgressBar(self, length=200, mode='determinate')
        self.progressbar.pack(pady=5)
        self.progressbar.widget['value'] = 50

        self.slider = FluentSlider(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.slider.pack(pady=5)

        self.toggle_switch = FluentToggleSwitch(self, command=self.on_toggle)
        self.toggle_switch.pack(pady=5)

        self.panel = FluentPanel(self, side=tk.RIGHT)
        self.panel_button = FluentButton(self, text="Toggle Panel", command=self.panel.toggle)
        self.panel_button.pack(pady=5)

        self.message_bar = FluentMessageBar(self, message="This is an info message")
        self.message_bar.show()

        self.command_bar = FluentCommandBar(self, commands=[
            {"label": "New", "action": self.on_new},
            {"label": "Open", "action": self.on_open},
            {"label": "Save", "action": self.on_save}
        ])
        self.command_bar.pack(fill=tk.X, pady=5)

        self.search_box = FluentSearchBox(self, command=self.on_search)
        self.search_box.pack(pady=5)

        self.spinner = FluentSpinner(self)
        self.spinner.pack(pady=5)
        self.spinner.start()

        self.pivot = FluentPivot(self, tabs=[
            {"label": "Tab 1", "content": self.create_tab1},
            {"label": "Tab 2", "content": self.create_tab2}
        ])
        self.pivot.pack(fill=tk.BOTH, expand=True, pady=5)

        self.dialog_button = FluentButton(self, text="Open Dialog", command=self.open_dialog)
        self.dialog_button.pack(pady=5)

        self.theme_dropdown = FluentDropdown(self, values=list(fluent_colors.THEMES.keys()))
        self.theme_dropdown.pack(pady=5)
        self.theme_button = FluentButton(self, text="Change Theme", command=self.change_theme)
        self.theme_button.pack(pady=5)

    def create_tab1(self, parent):
        return FluentLabel(parent, text="This is Tab 1 content")

    def create_tab2(self, parent):
        return FluentLabel(parent, text="This is Tab 2 content")

    def on_button_click(self):
        print("Button clicked!")
        print(f"Text field value: {self.text_field.get()}")
        print(f"Checkbox value: {self.checkbox.get()}")
        print(f"Radio value: {self.radio_var.get()}")
        print(f"Dropdown value: {self.dropdown.get()}")

    def on_new(self):
        print("New action")

    def on_open(self):
        print("Open action")

    def on_save(self):
        print("Save action")

    def on_search(self, query):
        print(f"Search query: {query}")

    def on_toggle(self):
        print("Toggle switched:", self.toggle_switch.switched_on)

    def open_dialog(self):
        dialog = FluentDialog(self, title="Example Dialog", message="This is a Fluent UI dialog.")
        result = dialog.show()
        print(f"Dialog result: {result}")

    def change_theme(self):
        new_theme = self.theme_dropdown.get()
        set_theme(new_theme)
        self.update_all_widgets()

    def update_all_widgets(self):
        for widget in self.winfo_children():
            if hasattr(widget, 'update_style'):
                widget.update_style()
        self.configure(bg=fluent_colors.BACKGROUND)

if __name__ == "__main__":
    app = BasicApp()
    app.mainloop()