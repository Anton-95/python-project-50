import json
import yaml


def load_file(path_file):
    if path_file.endswith('yaml') or path_file.endswith('yml'):
        with open(path_file, 'r') as yml_file:
            file = yaml.safe_load(yml_file)
    else:
        file = json.load(open(path_file))
    return file
