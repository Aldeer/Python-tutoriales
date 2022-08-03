# 4. Crear carpetas usando python

import os
from pathlib import Path, PurePath

""" os.mkdir("datos") """

# La diferencia con entre pathlib y os, es que con pathlib
# al metodo mkdir() le podemos agregar un parametro
# para saber si existe ya ese directorio y evitar que el
# programa arroje un error
Path("Datos").mkdir(exist_ok=True)

# agregar carpetas dentro de carpetas

""" os.makedirs(os.path.join("Dataset", "Scripts")) """

PurePath.joinpath(Path.cwd(), "Dataset2", "Scripts2").mkdir(parents=True)
