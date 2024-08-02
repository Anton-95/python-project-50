import json
import yaml


def load_file(path_file):
    if path_file.endswith(('yaml', 'yml')):
        with open(path_file, 'r') as yml_file:
            file = yaml.safe_load(yml_file)
            return file
    elif path_file.endswith('json'):
        file = json.load(open(path_file))
        return file
    else:
        raise ValueError("Unsupported file format. \
Expected '.yaml', '.yml' or '.json'.")
