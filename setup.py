import sys
from cx_Freeze import setup, Executable
import os
from pathlib import Path

icon_dir = Path() / "GUI" / "objects" / "icon"
font_dir = Path() / "GUI" / "objects" / "fonts"
icon_path = os.path.join(icon_dir, "calc.ico")
font_path = os.path.join(font_dir, "Digital7-1e1Z.ttf")

build_exe_options = {
    "packages": ["PySide6"],
    "excludes": ["tkinter"]
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MyPyCalculator",
    version="1.0",
    author="SkyArtur",
    description="Vintage Calculator!",
    options={"build_exe": build_exe_options},
    executables=[Executable("MyPyCalculator.py", icon=icon_path, base=base)],
)
