import os
from pathlib import Path

# Comprobando si existe una carpeta en el directorio actual con os
print(os.path.exists("Dataset"))

# Comrpobando si existe una carpeta en el directorio actual con pathlib

archivo = Path("data8")
print(archivo.exists())
