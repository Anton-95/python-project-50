import json
import yaml


def opened_files(path_file1, path_file2):
    if path_file1.endswith('yaml') or path_file1.endswith('yml'):
        with open(path_file1, 'r') as yml_file:
            file1 = yaml.safe_load(yml_file)
    else:
        file1 = json.load(open(path_file1))

    if path_file2.endswith('yaml') or path_file2.endswith('yml'):
        with open(path_file2, 'r') as yml_file:
            file2 = yaml.safe_load(yml_file)
    else:
        file2 = json.load(open(path_file2))
    return file1, file2


def make_sorted_string(dictionary):
    sorted_string = ''
    sorted_dict = dict(sorted(
        dictionary.items(), key=lambda x: (x[0].strip(' -+'), x[0][0])))
    for key, value in sorted_dict.items():
        sorted_string += f'{key}: {value}\n'
    return '{' + '\n' + sorted_string + '}'


def is_true_or_false(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
