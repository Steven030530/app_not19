# Libraries
import pandas as pd
import logging
from source.code.config import get_config
# Functions

def read_base_data(bd,sheet):

    try:
        config = get_config()
        input_file = config.get('DATA',bd)
        data = pd.read_excel(input_file,sheet_name=sheet)

        return data

    except FileNotFoundError as e:
        logging.error(f'No se encontro la ruta del archivo {e}')

