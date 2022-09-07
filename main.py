from pathlib import Path
import os
from secrets import *

ABS_PATH = Path(__file__).parent.absolute()
print(os.path.join(ABS_PATH, 'secrets.py'))
