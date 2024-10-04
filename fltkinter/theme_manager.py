from .colors import FluentColors

class ThemeManager:
    def __init__(self):
        self.colors = FluentColors()
        self.observers = []

    def set_theme(self, theme):
        self.colors.set_theme(theme)
        self.notify_observers()

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_style()

theme_manager = ThemeManager()