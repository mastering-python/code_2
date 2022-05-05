import os
import json
from logging import config


name = os.path.splitext(__file__)[0]
json_filename = os.path.join(os.path.dirname(__file__),
                             f'{name}.json')
with open(json_filename) as fh:
    config.dictConfig(json.load(fh))


