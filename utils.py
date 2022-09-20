import os
import configparser
from pathlib import Path

ABS_PATH = Path(__file__).parent.absolute()

def setup_config():
    country = input("Enter Country: ")
    config = configparser.ConfigParser()
    config['SERVER'] = {
        'API_KEY': 'SAMPLE_API_KEY',
    }
    config['API'] = {
        'COUNTRY': country,
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
