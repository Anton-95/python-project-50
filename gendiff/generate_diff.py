import json


def generate_diff(path_file1, path_file2):

    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    result_dict = {}

    for key, value in file1.items():
        value = is_true_or_false(value)
        if file2.get(key) == file1[key]:
            result_dict[f'    {key}'] = value
        elif file2.get(key) is None:
            result_dict[f'  - {key}'] = value
        elif file2.get(key) != file1[key] is not None:
            result_dict[f'  - {key}'] = value
            result_dict[f'  + {key}'] = file2[key]

    for key, value in file2.items():
        value = is_true_or_false(value)
        if file1.get(key) is None:
            result_dict[f'  + {key}'] = value

    return '{' + '\n' + make_sorted_string(result_dict) + '}'


def make_sorted_string(dictionary):
    sorted_string = ''
    sorted_dict = dict(sorted(
        dictionary.items(), key=lambda x: (x[0].strip(' -+'), x[0][0])))
    for key, value in sorted_dict.items():
        sorted_string += f'{key}: {value}\n'
    return sorted_string


def is_true_or_false(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
