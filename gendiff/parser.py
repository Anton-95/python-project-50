import json
import yaml
import os


def get_file_extension(file):
    return os.path.splitext(file)[1]


def load_file(path_file):
    extension = get_file_extension(path_file)
    if extension in ('.yaml', '.yml'):
        with open(path_file, 'r') as yml_file:
            file = yaml.safe_load(yml_file)
            return file
    elif extension == '.json':
        file = json.load(open(path_file))
        return file
    else:
        raise ValueError("Unsupported file format. "
                         "Expected '.yaml', '.yml' or '.json'.")
