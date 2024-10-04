# Fluent UI color palette
PRIMARY = "#0078D4"
SECONDARY = "#2B88D8"
BACKGROUND = "#F3F2F1"
TEXT = "#323130"
DISABLED = "#A19F9D"

class FluentColors:
    THEMES = {
        "light": {
            "PRIMARY": "#0078D4",
            "SECONDARY": "#2B88D8",
            "BACKGROUND": "#F3F2F1",
            "TEXT": "#323130",
            "DISABLED": "#A19F9D"
        },
        "dark": {
            "PRIMARY": "#0078D4",
            "SECONDARY": "#2B88D8",
            "BACKGROUND": "#202020",
            "TEXT": "#FFFFFF",
            "DISABLED": "#6E6E6E"
        },
        "black_and_white": {
            "PRIMARY": "#000000",
            "SECONDARY": "#404040",
            "BACKGROUND": "#FFFFFF",
            "TEXT": "#000000",
            "DISABLED": "#808080"
        },
        "sepia": {
            "PRIMARY": "#704214",
            "SECONDARY": "#9C7A3C",
            "BACKGROUND": "#F4ECD8",
            "TEXT": "#5E2612",
            "DISABLED": "#A39081"
        },
        "forest": {
            "PRIMARY": "#2C5F2D",
            "SECONDARY": "#4CAF50",
            "BACKGROUND": "#E8F5E9",
            "TEXT": "#1B5E20",
            "DISABLED": "#A5D6A7"
        }
    }

    def __init__(self, theme="light"):
        self.theme = theme
        self.update_colors()

    def update_colors(self):
        for key, value in self.THEMES[self.theme].items():
            setattr(self, key, value)

    def set_theme(self, theme):
        if theme in self.THEMES:
            self.theme = theme
            self.update_colors()
        else:
            raise ValueError(f"Theme '{theme}' not found. Available themes: {', '.join(self.THEMES.keys())}")

fluent_colors = FluentColors()