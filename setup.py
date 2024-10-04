from setuptools import setup, find_packages

setup(
    name="fltkinter",
    # ... 其他设置保持不变
    packages=find_packages(exclude=["examples"]),
    # ...
)