import tkinter as tk
from fluent_tkinter import (
    FluentButton, FluentTextField, FluentCheckbox, FluentLabel,
    FluentDropdown, FluentPanel, FluentMessageBar, FluentCommandBar,
    FluentDialog, FluentPivot, FluentSearchBox,
    set_theme, theme_manager, FluentLayout
)

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fluent UI Todo App")
        self.geometry("800x600")
        self.configure(bg=theme_manager.colors.BACKGROUND)

        self.todos = []
        self.create_widgets()

    def create_widgets(self):
        # Command Bar
        self.command_bar = FluentCommandBar(self, commands=[
            {"label": "Add Task", "action": self.show_add_task_dialog},
            {"label": "Clear Completed", "action": self.clear_completed_tasks},
            {"label": "Change Theme", "action": self.show_theme_dialog}
        ])
        FluentLayout.pack(self.command_bar, side=tk.TOP, fill=tk.X)

        # Search Box
        self.search_box = FluentSearchBox(self, placeholder="Search tasks...", command=self.search_tasks)
        FluentLayout.pack(self.search_box, side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Todo List
        self.todo_list = FluentPanel(self)
        FluentLayout.pack(self.todo_list, side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Message Bar
        self.message_bar = FluentMessageBar(self, message="Welcome to Fluent UI Todo App!")
        FluentLayout.pack(self.message_bar, side=tk.BOTTOM, fill=tk.X)

    def show_add_task_dialog(self):
        dialog = FluentDialog(self, title="Add Task")
        task_entry = FluentTextField(dialog.widget, placeholder="Enter task...")
        FluentLayout.pack(task_entry, pady=10)
        
        priority_label = FluentLabel(dialog.widget, text="Priority:")
        FluentLayout.pack(priority_label)
        
        priority_dropdown = FluentDropdown(dialog.widget, values=["Low", "Medium", "High"])
        FluentLayout.pack(priority_dropdown, pady=5)
        
        def add_task():
            task = task_entry.get()
            priority = priority_dropdown.get()
            if task:
                self.add_task(task, priority)
                dialog.widget.destroy()

        add_button = FluentButton(dialog.widget, text="Add", command=add_task)
        FluentLayout.pack(add_button, pady=10)
        
        dialog.show()

    def add_task(self, task, priority):
        todo_item = FluentCheckbox(self.todo_list.widget, text=f"{task} ({priority})")
        FluentLayout.pack(todo_item, anchor=tk.W, pady=2)
        self.todos.append(todo_item)
        self.message_bar.show(message=f"Task added: {task}")

    def clear_completed_tasks(self):
        completed_tasks = [todo for todo in self.todos if todo.get()]
        for task in completed_tasks:
            task.widget.destroy()
        self.todos = [todo for todo in self.todos if not todo.get()]
        self.message_bar.show(message=f"Cleared {len(completed_tasks)} completed tasks")

    def search_tasks(self, query):
        for todo in self.todos:
            if query.lower() in todo.widget.cget("text").lower():
                todo.widget.pack(anchor=tk.W, pady=2)
            else:
                todo.widget.pack_forget()

    def show_theme_dialog(self):
        dialog = FluentDialog(self, title="Change Theme")
        theme_dropdown = FluentDropdown(dialog.widget, values=list(theme_manager.colors.THEMES.keys()))
        FluentLayout.pack(theme_dropdown, pady=10)
        
        def change_theme():
            new_theme = theme_dropdown.get()
            set_theme(new_theme)
            self.update_all_widgets()
            dialog.widget.destroy()

        change_button = FluentButton(dialog.widget, text="Change", command=change_theme)
        FluentLayout.pack(change_button, pady=10)
        
        dialog.show()

    def update_all_widgets(self):
        for widget in self.winfo_children():
            if hasattr(widget, 'update_style'):
                widget.update_style()
        self.configure(bg=theme_manager.colors.BACKGROUND)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()