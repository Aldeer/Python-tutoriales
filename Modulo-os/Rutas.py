# Como obtener la ruta de trabajo
import os
from pathlib import Path

# 1. nombre de ruta de script de python

print(os.getcwd())
print(type(os.getcwd()))

print(Path.cwd())
print(type(Path.cwd()))
