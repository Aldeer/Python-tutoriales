"""
  Listar Archivos de una ruta 
"""

import os
from pathlib import Path

# 2.
print("Listado de archivos con OS:")
print(os.listdir())
# print(os.listdir("Tkinter"))

print("\nListado de archivos con pathlib")
print(list(Path().iterdir()))
# print(list(Path("Tkinter").iterdir()))
