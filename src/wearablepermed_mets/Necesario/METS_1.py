
import os
import numpy as np


# Definir ruta y nombre del archivo
ruta = "C:\\Users\\pablo\\Git\\uniovi-simur-datos\\PMP1047"
archivo = "data_tot.npz"

# Unir la ruta completa del archivo
ruta_completa = os.path.join(ruta, archivo)


data = np.load(ruta_completa)

# Ver las claves almacenadas en el archivo
print("Claves disponibles en el archivo .npz:", data.files)
