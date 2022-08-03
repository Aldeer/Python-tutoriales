import os
from pathlib import Path


print(os.path.abspath("Dataset"))

script = Path("2022-prueba_1.csv")

# Ruta absoluta
print(script.resolve())
# Nombre del archivo
print(script.stem)
# Extension del archivo
print(script.suffix)
# tamaño del archivo
print(script.stat().st_size)
