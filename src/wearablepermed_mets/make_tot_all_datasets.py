import os
import glob
import sys

import argparse
import logging

import re

import numpy as np
from scipy.interpolate import interp1d

__author__ = "Pablo Laviana <uo283485@uniovi.es>"
__copyright__ = "Uniovi"
__license__ = "MIT"


def generar_npz_mets_muneca_muslo(ruta_carpeta_PMPs):

    carpetas_pmp = []

    for nombre in os.listdir(ruta_carpeta_PMPs):
        
        if (os.path.isdir(os.path.join(ruta_carpeta_PMPs, nombre)) and nombre.startswith("PMP")):

            carpetas_pmp.append(nombre)

    # Se recorren las carpetas
    for carpeta in carpetas_pmp:

        ruta_completa_PMP = os.path.join(ruta_carpeta_PMPs, carpeta)
        print(f"***** Procesando carpeta: {ruta_completa_PMP}")

        try:
            # Listar los archivos de cada PMP
            lista_archivos = os.listdir(ruta_completa_PMP)
            
            # Buscar archivos que contengan '_M_tot'
            lista_archivos_tot_M_features_mets = [f for f in lista_archivos if '_tot_M_features_mets' in f]

            # Buscar archivos que contengan '_PI_tot'
            lista_archivos_tot_PI_features_mets = [f for f in lista_archivos if '_tot_PI_features_mets' in f]

            # Verificar que existan ambos archivos
            if not lista_archivos_tot_M_features_mets or not lista_archivos_tot_PI_features_mets:

                print(f"Faltan archivos en la carpeta {carpeta}, se omite esta carpeta.")
                
                if not lista_archivos_tot_M_features_mets:
                    print(f"Falta archivo tot_M_features_mets")
                
                if not lista_archivos_tot_M_features_mets:
                    print(f"Falta archivo tot_PI_features_mets")

                continue  # Salta a la siguiente carpeta
            
            # Cargar datos de _tot_M_features_mets
            ruta_tot_M_features_mets = glob.glob(os.path.join(ruta_completa_PMP, lista_archivos_tot_M_features_mets[0]))[0]

            tot_M_features_mets = np.load(ruta_tot_M_features_mets)

            X_tot_M_features_mets = tot_M_features_mets['arr0']
            y_tot_M_features_mets = tot_M_features_mets['arr1']


            # Cargar datos de _tot_PI_features_mets
            ruta_tot_PI_features_mets = glob.glob(os.path.join(ruta_completa_PMP, lista_archivos_tot_PI_features_mets[0]))[0]

            tot_PI_features_mets = np.load(ruta_tot_PI_features_mets)

            X_tot_PI_features_mets = tot_PI_features_mets['arr0']
            y_tot_PI_features_mets = tot_PI_features_mets['arr1']

            # Interpolar por si hay diferencia de tiempos
            if len(y_tot_M_features_mets) >= len(y_tot_PI_features_mets):

                y_objetivo = y_tot_M_features_mets
                # Interpolar X_PI
                interpolador_PI = interp1d(y_tot_PI_features_mets, X_tot_PI_features_mets, axis=0, kind='linear', fill_value="extrapolate")
                X_PI_interp = interpolador_PI(y_objetivo)
                X_concat = np.concatenate((X_tot_M_features_mets, X_PI_interp), axis=1)
                
            else:
                y_objetivo = y_tot_PI_features_mets
                # Interpolar X_M
                interpolador_M = interp1d(y_tot_M_features_mets, X_tot_M_features_mets, axis=0, kind='linear', fill_value="extrapolate")
                X_M_interp = interpolador_M(y_objetivo)
                X_concat = np.concatenate((X_M_interp, X_tot_PI_features_mets), axis=1)

            print(X_tot_M_features_mets.shape, X_tot_PI_features_mets.shape)
            _logger.info(X_concat.shape)

            X_PI_M = X_concat 
            y_PI_M = y_objetivo

            # Guardar el archivo con un nombre completo

            # Extraemos el nombre del archivo original
            nombre_archivo = os.path.basename(ruta_tot_M_features_mets)

            # Extraemos la carpeta donde se encuentra el archivo original
            carpeta_destino = os.path.dirname(ruta_tot_M_features_mets)

            # Usar regex para extraer número y letra
            match = re.search(r"data_(\d+)_tot_([A-Z])_features_mets", nombre_archivo)

            print(ruta_completa_PMP)

            if match:
                numero = match.group(1)
                
                nuevo_nombre = f"data_{numero}_tot_all_features_mets.npz"
                ruta_guardado = os.path.join(carpeta_destino, nuevo_nombre)

                # Guardar el archivo
                np.savez(ruta_guardado, arr0=X_PI_M, arr1=y_PI_M)

                print(f"Archivo guardado en: {ruta_guardado}")

            else:
                print("No se pudo extraer número y letra del nombre del archivo.")

        except Exception as e:
            print(f"Error procesando carpeta {carpeta}: {e}")
            print("Se continúa con la siguiente carpeta.")

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
        "-ruta-carpeta-PMPs",
        "--ruta-carpeta-PMPs",
        dest="ruta_carpeta_PMPs",
        required=True,
        help="Ruta a la carpeta que contiene a todos los participantes."
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

    _logger.info(" make_tot_all_datasets starts here\n")


    generar_npz_mets_muneca_muslo(
        args.ruta_carpeta_PMPs
    )

    _logger.info(" make_tot_all_datasets ends here\n")

def run():

    # Los args estan en .vscode launch
    main(sys.argv[1:])

_logger = logging.getLogger(__name__)

# Se ejecuta si es el principial; y no, si es usado como modulo
if __name__ == "__main__":

    run()







