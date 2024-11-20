"""Creates an executable for the `main.py` script using PyInstaller."""

import PyInstaller.__main__

# Define PyInstaller arguments
arguments = [
    "main.py",
    "--clean",
    "--onefile",
    "-n", "Cleaner",
    "--noconsole",
    "-i", "icon.ico"]

# Run PyInstaller with the specified arguments
PyInstaller.__main__.run(arguments)
