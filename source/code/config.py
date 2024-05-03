import os
from configparser import ConfigParser

def get_config():
    env = os.environ.get('ENV','dev')
    config = ConfigParser()
    config.read(f'source/code/{env}.cfg')
    return config

