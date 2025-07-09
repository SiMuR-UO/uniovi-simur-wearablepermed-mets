import os
import glob

import numpy as np
import random

from tensorflow import keras
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


def entrenar_muslo(ruta_output, nombre_caso, participantes_entrenamiento, base_path):

    # Crear funcion train Muneca
    ruta_caso = os.path.join(ruta_output, nombre_caso)

    # Listar los archivos de cada caso
    lista_archivos = os.listdir(ruta_caso)

    # Buscar archivos que contengan '_M_tot'
    lista_archivos_M_features_mets = [f for f in lista_archivos if 'data_all_tot_M_features_mets' in f]

    # Buscar archivos que contengan '_PI_tot'
    lista_archivos_PI_features_mets = [f for f in lista_archivos if 'data_all_tot_PI_features_mets' in f]

    # Buscar archivos que contengan '_PI_tot'
    lista_archivos_all_features_mets = [f for f in lista_archivos if 'data_all_tot_all_features_mets' in f]

    if not lista_archivos_M_features_mets or not lista_archivos_PI_features_mets or not lista_archivos_all_features_mets:

        print(f"Faltan archivos en la carpeta")
        
        if not lista_archivos_M_features_mets:
            print(f"Falta archivo data_all_tot_M_features_met")
        
        if not lista_archivos_PI_features_mets:
            print(f"Falta archivo _PI_features_mets")

        if not lista_archivos_all_features_mets:
            print(f"Falta archivo _all_features_mets")




    # Se carga el modelos
    ruta_modelo_red_Muslo_transferLearning = (os.path.join(base_path, './modelos/modelo_red_Muslo_transferLearning.h5'))
    modelo_red_Muslo_transferLearning = load_model(ruta_modelo_red_Muslo_transferLearning)
    modelo_red_Muslo_transferLearning.summary()

    # Se cargan los datos Muneca
    ruta_PI_features_mets = glob.glob(os.path.join(ruta_caso, lista_archivos_PI_features_mets[0]))[0]

    data_ruta_PI_features_mets = np.load(ruta_PI_features_mets)

    X_PI = data_ruta_PI_features_mets['arr0']
    y_PI = data_ruta_PI_features_mets['arr1']
    actividades_PI = data_ruta_PI_features_mets['arr2']
    id_participante_PI = data_ruta_PI_features_mets['arr3']


    # Se crea un modelo final que se ira reentrenando
    modelo_final_Muslo = modelo_red_Muslo_transferLearning
    ruta_guardado = os.path.join(ruta_caso, 'modelo_final_Muslo.h5')
    modelo_final_Muslo.save(ruta_guardado)
    modelo_final_Muslo = load_model(ruta_guardado)

    # Se crea una mascara que incluye solo los participantes indicados
    mascara_combinada = np.zeros(id_participante_PI.shape[0], dtype=bool)

    for participante in participantes_entrenamiento:

        mascara = (id_participante_PI.flatten() == participante)
        mascara_combinada |= mascara

    # Aplicar la máscara para obtener los datos correspondientes al participante
    X_participantes = X_PI[mascara_combinada.flatten()]
    y_participantes = y_PI[mascara_combinada.flatten()]
    actividades_participantes = actividades_PI[mascara_combinada.flatten()]
    id_participantes = id_participante_PI[mascara_combinada.flatten()]

    # Entrenar con los datos de ese participante
    random = 42

    scaler = StandardScaler()
    X_norm = scaler.fit_transform(X_participantes)

    modelo_final_Muslo.compile(optimizer='adam', loss='mean_squared_error', metrics=[keras.metrics.MeanSquaredError()])
    modelo_final_Muslo.fit(X_norm, y_participantes, epochs=100, batch_size=256, verbose=1)

    y_pred_train_muSLO = modelo_final_Muslo.predict(X_norm)
    r2_train = r2_score(y_participantes, y_pred_train_muSLO)
    mse_train = mean_squared_error(y_participantes, y_pred_train_muSLO)

    # Guardar el valor de mse de train
    ruta_train_muslo = os.path.join(ruta_caso, 'mse_train_muslo.txt')

    # Guardar ambos valores en un archivo de texto
    with open(ruta_train_muslo, 'w') as f:
        f.write(f'Participantes: {participantes_entrenamiento}\n')
        f.write(f'MSE Train: {mse_train:.5f}\n')
        f.write(f'R2 Train: {r2_train:.5f}\n')

    print(f"Las predicciones se han guardado en: {ruta_train_muslo}")

