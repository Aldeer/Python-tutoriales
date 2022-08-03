

import os
from pathlib import Path

# 5. Renombrar archivos con OS

""" os.rename("Dataset", "Data") """

# Renombrar con path

""" path_actual = Path("Data")
path_objetivo = Path("Dataset")

Path.rename(path_actual, path_objetivo) """


for file in os.listdir():
    if file.endswith(".csv"):
        os.rename(file, f"2022-{file}")
