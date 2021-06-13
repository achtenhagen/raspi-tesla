import os

import toml


def load_config(file):
    file_path = f'config/{file}'
    if not os.path.exists(file_path):
        raise Exception(f'{file_path} does not exist!')
    else:
        return toml.load(file_path)
