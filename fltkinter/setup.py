from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fltkinter",
    version="0.1.0",
    author="SoulCodingYanhun",
    author_email="zhuzhishengzhu6@outlook.com",
    description="A Fluent UI styled widget library for Tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SoulCodingYanhun/fltkinter",
    packages=find_packages(exclude=["examples"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "tkinter",
    ],
)