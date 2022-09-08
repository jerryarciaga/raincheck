import os
import configparser
from pathlib import Path

ABS_PATH = Path(__file__).parent.absolute()

config = configparser.ConfigParser()
config['SERVER'] = {
    'API_KEY': 'SAMPLE_API_KEY',
}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
