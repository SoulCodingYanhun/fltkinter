# Fluent UI Tkinter 使用文档

## 目录
1. 简介
2. 安装
3. 基本用法
4. 组件概述
5. 主题管理
6. 高级用法
7. 示例应用

## 1. 简介

Fluent UI Tkinter 是一个 Python 库，旨在为 Tkinter 应用程序带来 Fluent UI 设计语言的风格和功能。它提供了一套自定义的小部件和工具，使开发者能够创建现代、视觉吸引力强的用户界面。

## 2. 安装

使用 pip 安装 Fluent UI Tkinter：

``` bash
pip install fltkinter
```

## 3. 基本用法

以下是一个简单的示例，展示了如何使用 Fluent UI Tkinter 创建一个基本的应用程序：
``` python
import tkinter as tk
from fltkinter import FluentButton, FluentTextField, set_theme
class MyApp(tk.Tk):
    def init(self):
        super().init()
        self.title("My Fluent UI App")
        self.geometry("300x200")
        self.text_field = FluentTextField(self, placeholder="Enter your name")
        self.text_field.pack(pady=20)
        self.button = FluentButton(self, text="Say Hello", command=self.say_hello)
        self.button.pack()
    def say_hello(self):
        name = self.text_field.get()
        print(f"Hello, {name}!")
        if name == "main":
            set_theme("light")
app = MyApp()
app.mainloop()
```

## 4. 组件概述

Fluent UI Tkinter 提供了以下组件：

- FluentButton: 按钮
- FluentTextField: 文本输入框
- FluentCheckbox: 复选框
- FluentRadio: 单选按钮
- FluentLabel: 标签
- FluentDropdown: 下拉菜单
- FluentProgressBar: 进度条
- FluentSlider: 滑块
- FluentToggleSwitch: 开关
- FluentChoiceGroup: 选项组
- FluentPanel: 面板
- FluentMessageBar: 消息栏
- FluentCommandBar: 命令栏
- FluentDialog: 对话框
- FluentPivot: 选项卡
- FluentSearchBox: 搜索框
- FluentSpinner: 加载动画

每个组件都继承自 FluentWidget 基类，并提供了 update_style() 方法以支持主题切换。

## 5. 主题管理

Fluent UI Tkinter 支持多种主题，包括：

- light（默认）
- dark
- black_and_white
- sepia
- forest

要设置或更改主题，使用 set_theme() 函数：
``` python
from fltkinter import set_theme
set_theme("dark")
```

## 6. 高级用法

### 6.1 布局管理

Fluent UI Tkinter 提供了 FluentLayout 类来简化布局管理：

``` python
from fltkinter import FluentLayout
FluentLayout.pack(widget, side=tk.TOP, fill=tk.X, padx=10, pady=10)
FluentLayout.grid(widget, row=0, column=0, padx=5, pady=5)
FluentLayout.place(widget, x=10, y=10)
```

### 6.2 异常处理

库提供了自定义异常类：

- FluentUIError: 基础异常类
- ThemeError: 主题相关错误
- WidgetError: 组件相关错误

### 6.3 配置管理

ConfigManager 类用于保存和加载用户首选项：
```python
from fltkinter import config_manager
config_manager.set("theme", "dark")
current_theme = config_manager.get("theme", default="light")
```

## 7. 示例应用

为了更好地理解如何使用 Fluent UI Tkinter，请查看 examples 目录中的示例应用：

- basic_app.py: 展示了大多数组件的基本用法
- todo_app.py: 一个功能性的待办事项应用，展示了更复杂的用法

### Todo App 示例

todo_app.py 展示了如何创建一个功能性的待办事项应用。它包括以下功能：

- 添加新任务
- 标记任务为完成
- 删除已完成的任务
- 搜索任务
- 更改主题

要运行这个示例，请执行以下命令：
``` bash 
python examples/todo_app.py
```

这个示例展示了如何组合使用多个 Fluent UI 组件来创建一个完整的应用程序，包括：

- 使用 FluentCommandBar 创建主要操作按钮
- 使用 FluentSearchBox 实现任务搜索功能
- 使用 FluentPanel 作为任务列表的容器
- 使用 FluentMessageBar 显示操作反馈
- 使用 FluentDialog 创建添加任务和更改主题的对话框
- 使用 FluentTextField 输入新任务
- 使用 FluentDropdown 选择任务优先级和主题
- 使用 FluentCheckbox 表示每个任务
- 实现主题切换功能

通过学习这个示例，您可以了解如何将各种 Fluent UI 组件组合在一起，创建功能丰富、外观现代的应用程序。
