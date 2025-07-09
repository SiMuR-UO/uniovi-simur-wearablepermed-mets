import os
import glob
import sys

import argparse
import logging

import re

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

__author__ = "Pablo Laviana <uo283485@uniovi.es>"
__copyright__ = "Uniovi"
__license__ = "MIT"


def columna_excel(string_columna, Actividades, path_excel_FASE_REPOSO_CON_K5, path_excel_TAPIZ_RODANTE, path_excel_SIT_TO_STAND_30_s, path_excel_INCREMENTAL_CICLOERGOMETRO):
    
    # Reposo con K5
    excel_FASE_REPOSO_CON_K5 = pd.read_excel(path_excel_FASE_REPOSO_CON_K5, engine='openpyxl')
    excel_METS_FASE_REPOSO_CON_K5 = pd.to_numeric(excel_FASE_REPOSO_CON_K5[string_columna][2:], errors='coerce')

    indices_reposo = np.where(Actividades == 'FASE REPOSO CON K5')[0]
    num_reposo = len(indices_reposo)

    METS_FASE_REPOSO_CON_K5 = np.interp(np.linspace(0, len(excel_METS_FASE_REPOSO_CON_K5) - 1, num_reposo),
                                        np.arange(len(excel_METS_FASE_REPOSO_CON_K5)),
                                        excel_METS_FASE_REPOSO_CON_K5)
    
    # Tapiz rodante
    excel_TAPIZ_RODANTE = pd.read_excel(path_excel_TAPIZ_RODANTE, engine='openpyxl')
    excel_METS_TAPIZ_RODANTE = pd.to_numeric(excel_TAPIZ_RODANTE[string_columna][2:], errors='coerce')

    indices_reposo = np.where(Actividades == 'TAPIZ RODANTE')[0]
    num_reposo = len(indices_reposo)

    METS_TAPIZ_RODANTE = np.interp(np.linspace(0, len(excel_METS_TAPIZ_RODANTE) - 1, num_reposo),
                                        np.arange(len(excel_METS_TAPIZ_RODANTE)),
                                        excel_METS_TAPIZ_RODANTE)
    
    # Sit to stand
    excel_SIT_TO_STAND_30_s = pd.read_excel(path_excel_SIT_TO_STAND_30_s, engine='openpyxl')
    excel_METS_SIT_TO_STAND_30_s = pd.to_numeric(excel_SIT_TO_STAND_30_s[string_columna][2:], errors='coerce')

    indices_reposo = np.where(Actividades == 'SIT TO STAND 30 s')[0]
    num_reposo = len(indices_reposo)

    METS_SIT_TO_STAND_30_s = np.interp(np.linspace(0, len(excel_METS_SIT_TO_STAND_30_s) - 1, num_reposo), 
                                       np.arange(len(excel_METS_SIT_TO_STAND_30_s)), 
                                       excel_METS_SIT_TO_STAND_30_s)
    
    # Incremental cicloergometro
    excel_INCREMENTAL_CICLOERGOMETRO = pd.read_excel(path_excel_INCREMENTAL_CICLOERGOMETRO, engine='openpyxl')
    excel_METS_INCREMENTAL_CICLOERGOMETRO = pd.to_numeric(excel_INCREMENTAL_CICLOERGOMETRO[string_columna][2:], errors='coerce')

    indices_reposo = np.where(Actividades == 'INCREMENTAL CICLOERGOMETRO')[0]
    num_reposo = len(indices_reposo)

    METS_INCREMENTAL_CICLOERGOMETRO = np.interp(np.linspace(0, len(excel_METS_INCREMENTAL_CICLOERGOMETRO) - 1, num_reposo),
                                                np.arange(len(excel_METS_INCREMENTAL_CICLOERGOMETRO)),
                                                excel_METS_INCREMENTAL_CICLOERGOMETRO)

    # Concatenar todos
    y_METS = np.concatenate([
        METS_FASE_REPOSO_CON_K5,
        METS_TAPIZ_RODANTE,
        METS_SIT_TO_STAND_30_s,
        METS_INCREMENTAL_CICLOERGOMETRO
    ])
 
    return y_METS

def generar_npz_mets(ruta_datos_features, ruta_excel_FASE_REPOSO_CON_K5, ruta_excel_TAPIZ_RODANTE, 
                    ruta_excel_SIT_TO_STAND_30_s, ruta_excel_INCREMENTAL_CICLOERGOMETRO):

    print(f"Generando METS: ")

    try:

        # Importamos los datos
        data = np.load(ruta_datos_features)
        X = data['arr_0']
        y_Actividades = data['arr_1']

        print(np.isnan(X).sum(), np.isinf(X).sum())

        # Obtenemos los METs
        y_METS = columna_excel('METS', y_Actividades, ruta_excel_FASE_REPOSO_CON_K5, ruta_excel_TAPIZ_RODANTE, ruta_excel_SIT_TO_STAND_30_s, ruta_excel_INCREMENTAL_CICLOERGOMETRO)

        # Se consigue reescalar el dataset para que coincida con los METs
        X_con_METS = X[:len(y_METS)]
        y_Actividades_METS = y_Actividades[:len(y_METS)]

        # Procesamos los datos
        # 1º que no haya nans
        mask = ~np.isnan(X_con_METS).any(axis=1)

        X_con_METS = X_con_METS[mask]
        y_METS = y_METS[mask]
        y_Actividades_METS = y_Actividades_METS[mask]

        print(X_con_METS.shape, y_Actividades_METS.shape, y_METS.shape)

        # Extraemos el nombre del archivo original
        nombre_archivo = os.path.basename(ruta_datos_features)

        # Extraemos la carpeta donde se encuentra el archivo original
        carpeta_destino = os.path.dirname(ruta_datos_features)

        # Usar regex para extraer número y letra
        nuevo_nombre = nombre_archivo.replace(".npz", "_mets.npz")

        ruta_guardado = os.path.join(carpeta_destino, nuevo_nombre)

        # Guardar el archivo
        np.savez(ruta_guardado, arr0=X_con_METS, arr1=y_METS, arr2 = y_Actividades_METS)

        print(f"Archivo guardado en: {ruta_guardado}")

        #else:
        #    print("No se pudo extraer número y letra del nombre del archivo.")

    except Exception as e:
    
        print(f"Error creando archivo npz: {ruta_datos_features} -> {e}")

    return

def setup_logging(loglevel):

    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )

# Argumentos de entrada para llamar al modulo
def parse_args(args):
    parser = argparse.ArgumentParser(description="Machine Learning Model Trainer")

    parser.add_argument(
        "-ruta-datos-features",
        "--ruta-datos-features",
        dest="ruta_datos_features",
        required=True,
        help="Ruta al archivo .npz de datos con features."
    )

    parser.add_argument(
        "-ruta-excel-fase-reposo",
        "--ruta-excel-fase-reposo",
        dest="ruta_excel_FASE_REPOSO_CON_K5",
        required=True,
        help="Ruta al Excel de la fase de reposo con K5."
    )

    parser.add_argument(
        "-ruta-excel-tapiz-rodante",
        "--ruta-excel-tapiz-rodante",
        dest="ruta_excel_TAPIZ_RODANTE",
        required=True,
        help="Ruta al Excel del test en tapiz rodante."
    )

    parser.add_argument(
        "-ruta-excel-sts",
        "--ruta-excel-sts",
        dest="ruta_excel_SIT_TO_STAND_30_s",
        required=True,
        help="Ruta al Excel del test Sit-To-Stand de 30 segundos."
    )

    parser.add_argument(
        "-ruta-excel-incremental-cicloergometro",
        "--ruta-excel-incremental-cicloergometro",
        dest="ruta_excel_INCREMENTAL_CICLOERGOMETRO",
        required=True,
        help="Ruta al Excel del test incremental en cicloergómetro."
    )

    parser.add_argument(
        "--loglevel",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level"
    )


    return parser.parse_args(args)

def main(args):

    args = parse_args(args)

    setup_logging(args.loglevel)

    _logger.info(" Windowing METS starts here\n")


    generar_npz_mets(
        args.ruta_datos_features,
        args.ruta_excel_FASE_REPOSO_CON_K5,
        args.ruta_excel_TAPIZ_RODANTE,
        args.ruta_excel_SIT_TO_STAND_30_s,
        args.ruta_excel_INCREMENTAL_CICLOERGOMETRO,
    )

    _logger.info(" Windowing METS ends here\n")

def run():

    # Los args estan en .vscode launch
    main(sys.argv[1:])

_logger = logging.getLogger(__name__)

# Se ejecuta si es el principial; y no, si es usado como modulo
if __name__ == "__main__":

    run()

