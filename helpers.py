import os
import json

def get_config():
    config = None
    filename = 'config.json'
    if os.path.isfile(filename):
        config = json.load(open(filename))
    else:
        print('No config.json found in directory!')
    return config

