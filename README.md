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

## Execute from Docker

     ```
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
