
import os
import glob

import numpy as np
import random

from tensorflow import keras
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


from trainers.trainer_muneca import entrenar_muneca
from trainers.trainer_muslo import entrenar_muslo
from trainers.trainer_muneca_muslo import entrenar_muneca_muslo

# Argumentos de entrada

ruta_output = r'C:\Users\pablo\Git\uniovi-simur-datos'

nombre_caso = 'Caso_1'

participantes_entrenamiento = ['PMP12', 'PMP21']


# Codigo

# Obtener la ruta del ejecutable
base_path = os.path.dirname(os.path.abspath(__file__))

entrenar_muneca(ruta_output, nombre_caso, participantes_entrenamiento, base_path)

entrenar_muslo(ruta_output, nombre_caso, participantes_entrenamiento, base_path)

entrenar_muneca_muslo(ruta_output, nombre_caso, participantes_entrenamiento, base_path)






# Mocks CREADO en local
# # Definir las constantes
# num_participantes = 22904
# num_features = 91
# actividades = ['sentado', 'corriendo', 'reposo']
# prefix_id = 'PMP'

# # Mock de X_M_participantes (números aleatorios)
# X_M_participantes = np.random.rand(num_participantes, num_features)

# # Mock de y_M_participantes (números aleatorios entre 0 y 1)
# y_M_participantes = np.random.randint(0, 2, size=(num_participantes, 1))

# # Mock de actividades_M_participantes (elegir aleatoriamente entre 'sentado', 'corriendo', 'reposo')
# actividades_M_participantes = np.array([random.choice(actividades) for _ in range(num_participantes)])
# actividades_M_participantes = actividades_M_participantes.reshape(-1, 1)

# # Mock de id_participante_M (secuencial 'PMP01', 'PMP02', ...)

# carpetas = [f"PMP{i+1}" for i in range(56)]  # Nombres de las carpetas
# id_participante_M = np.array([random.choice(carpetas) for _ in range(num_participantes)]).reshape(-1, 1)

# # id_participante_M = np.array([f"{prefix_id}{str(i+1).zfill(3)}" for i in range(num_participantes)])
# # id_participante_M = id_participante_M.reshape(-1, 1)


# print(X_M_participantes.shape)
# print(y_M_participantes.shape)
# print(actividades_M_participantes.shape)
# # print(id_participante_M.shape)

# import matplotlib.pyplot as plt

# # plt.plot(actividades_M_participantes)
# # plt.show()

# carpeta_destino = r'C:\Users\pablo\Git\uniovi-simur-datos\Caso_1'

# nuevo_nombre = f"mock_data_all_tot_M_features_mets.npz"
# ruta_guardado = os.path.join(carpeta_destino, nuevo_nombre)

# np.savez(ruta_guardado, arr0=X_M_participantes, arr1=y_M_participantes, arr2=actividades_M_participantes, arr3=id_participante_M)


# print(id_participante_M)




































