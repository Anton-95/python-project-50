import json
import yaml
import os


def get_file_extension(file):
    return os.path.splitext(file)[1]


def load_file(path_file):
    """
    Loads data from a file. Supported formats: YAML and JSON.

    Args:
        path_file (str): The path to the file to be loaded.

    Returns:
        dict: The data loaded from the file.

    Raises:
        ValueError: If the file format is not supported.
    """
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
