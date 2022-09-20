import os
import configparser
from pathlib import Path

ABS_PATH = Path(__file__).parent.absolute()

def setup_config():
    # User interface
    API_KEY = input("Enter API Key: ")
    country = input("Enter Country: ")

    config = configparser.ConfigParser()
    config['SERVER'] = {
        'API_KEY': API_KEY,
    }
    config['API'] = {
        'COUNTRY': country,
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
