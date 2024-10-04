class FluentUIError(Exception):
    """Base exception for FluentUI errors"""
    pass

class ThemeError(FluentUIError):
    """Raised when there's an error with theme operations"""
    pass

class WidgetError(FluentUIError):
    """Raised when there's an error with widget operations"""
    pass