#Libraries
import pandas as pd
import logging
from source.utils import setup_logging
#Functions

setup_logging()

def read_bd_employee(path_excel):

    try:
        data = pd.read_excel(path_excel)
        logging.info('Lectura de la base de datos de empleados exitosa!!!')
        return data
    except:
        logging.error('fallo lectura de la base de datos')
