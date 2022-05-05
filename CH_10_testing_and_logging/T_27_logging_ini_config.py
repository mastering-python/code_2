import os
from logging import config

name = os.path.splitext(__file__)[0]

config.fileConfig(os.path.join(os.path.dirname(__file__),
                  f'{name}.ini'))
