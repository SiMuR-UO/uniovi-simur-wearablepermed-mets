<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/uniovi-simur-wearablepermed-mets.svg?branch=main)](https://cirrus-ci.com/github/<USER>/uniovi-simur-wearablepermed-mets)
[![ReadTheDocs](https://readthedocs.org/projects/uniovi-simur-wearablepermed-mets/badge/?version=latest)](https://uniovi-simur-wearablepermed-mets.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/uniovi-simur-wearablepermed-mets/main.svg)](https://coveralls.io/r/<USER>/uniovi-simur-wearablepermed-mets)
[![PyPI-Server](https://img.shields.io/pypi/v/uniovi-simur-wearablepermed-mets.svg)](https://pypi.org/project/uniovi-simur-wearablepermed-mets/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/uniovi-simur-wearablepermed-mets.svg)](https://anaconda.org/conda-forge/uniovi-simur-wearablepermed-mets)
[![Monthly Downloads](https://pepy.tech/badge/uniovi-simur-wearablepermed-mets/month)](https://pepy.tech/project/uniovi-simur-wearablepermed-mets)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/uniovi-simur-wearablepermed-mets)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# uniovi-simur-wearablepermed-mets

> Uniovi Simur WearablePerMed metabolic expenditure

A longer description of your project goes here...


<!-- pyscaffold-notes -->

## Create venv in windows

      ```
     Open Anaconda Prompt
     Go to the git project folder ($ cd .....)
     $ python -m venv .venv                  
     $ .venv\Scripts\activate
     Do ($ conda deactivate) to remove (base)             
     ```

## How install packets in venv in Windows

     ```
     Open Anaconda Prompt
     Go to the git project folder ($ cd .....)
     Apply ($ .venv\Scripts\activate)
     Do ($ conda deactivate) to remove (base)

     Then, it is able to do ($ pip install ....)

     ($ exit) for exit
     ```

## Save dependencies in a requirements .txt

     ```
     $ pip freeze > requirements.txt
     ```

## Create venv in Linux and install the dependencies

      ```
     $ python3 -m venv .venv
     $ source .venv/bin/activate
     $ pip install -r requirements.txt
     ```

## Create dockerFile and Compile de image

     ```
     Imagen base: aunque sea python, es una distribucion de linux con un python instalado
     Crearse una carpeta /app en esa imagen de linux 
     Actualizar el git del linux
     Actualizar el pip

     Copiar de la carpeta donde se ubica el Dockefile el requirements
     Instalar con el pip el requirements

     Guardar el fichero de python el la carpeta /app de esa imagen de linux

     (CMD [ "sh" ]) Permite tener una shell, sin embargo, si se hace un docker run no se vería porque el contenedor
     se crea y se destruye. Para ver esa imagen de linux hay que añadir el parametro -it, que permite tener una shell
     interactiva y permite jugar con el linux. Todo lo que se quiera guardar de forma persistente deberia guardarse en un
     volumen en una ruta del host.

     ```



## Execute from Docker

     ```
     -v Volumenes: ruta que permite compartir archivos entre el host y el contenedor. Monta los archivos de la ruta del host (un Windows, un servidor linux ...) en la ruta deseada del contenedor (un linux que corre en el contenedor). Permite guardar datos importantes en el host aunque el contenedor muera. Hay que seguirlo del nombre del contenedor.
     python mas el nombre del fichero ejecutable
     Parámetros

     Ejemplo:

     $ docker run \
      -v /mnt/nvme1n2/git/uniovi-simur-wearablepermed-data/input:/app/data uniovi-simur-wearablepermed-mets:1.0.0 \
     python windowing_mets.py \
     --ruta-datos-features data/PMP1006/data_1006_tot_M_features.npz \
     --ruta-excel-fase-reposo 'data/PMP1006/PMP1006_REPOSO_20240927(CPET Cámara de Mezcla).xlsx' \
     --ruta-excel-tapiz-rodante 'data/PMP1006/PMP1006_TREADMILL_20240927(CPET Respiración a Respiración).xlsx' \
     --ruta-excel-sts 'data/PMP1006/PMP1006_STS_20240927(CPET Respiración a Respiración).xlsx' \
     --ruta-excel-incremental 'data/PMP1006/PMP1006_GXT_20240927(CPET Respiración a Respiración).xlsx'
     ```

## Note

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
