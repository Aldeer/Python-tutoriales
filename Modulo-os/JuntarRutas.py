from pathlib import Path, PurePath
import os


print(os.path.join(os.getcwd(), "Datos"))

print(PurePath.joinpath(Path.cwd(), "Datos"))
