from gendiff.formatters import stylish, plain, json
import json as jsn
import yaml


def generate_diff(path_file1, path_file2, formatter=stylish):
    file1, file2 = opening_files(path_file1, path_file2)

    def iter_(file1, file2):

        keys = file1.keys() | file2.keys()
        diff = []

        for key in keys:
            value1 = is_true_or_false_or_none(file1.get(key))
            value2 = is_true_or_false_or_none(file2.get(key))

            if not isinstance(value1, dict) and not isinstance(value2, dict):
                if key not in file1:
                    diff += [{'key': key,
                              'value': value2,
                              'status': 'added'}
                             ]
                elif key not in file2:
                    diff += [{'key': key,
                              'value': value1,
                              'status': 'deleted'}]
                elif value1 == value2:
                    diff += [{'key': key,
                              'value': value1,
                              'status': 'unchanged'}]
                else:
                    diff += [{'key': key,
                              'old_value': value1,
                              'new_value': value2,
                              'status': 'changed'}]

            elif isinstance(value1, dict) and isinstance(value2, dict):
                if value1 != value2:
                    diff += [{'key': key,
                              'children': iter_(value1, value2),
                              'status': 'unchanged'}]
                elif value1 == value2:
                    diff += [{'key': key,
                              'children': iter_(value1, value2),
                              'status': 'unchanged'}]

            elif not isinstance(value1, dict) and isinstance(value2, dict):
                if file1.get(key) is None:
                    diff += [{'key': key,
                              'children': iter_(value2, value2),
                              'status': 'added'}]
                elif value1 is not None:
                    diff += [{'key': key,
                              'old_value': value1,
                              'new_value': iter_(value2, value2),
                              'status': 'changed'}]

            elif isinstance(value1, dict) and not isinstance(value2, dict):
                if file2.get(key) is None:
                    diff += [{'key': key,
                              'children': iter_(value1, value1),
                              'status': 'deleted'}]
                elif value2 is not None:
                    diff += [{'key': key,
                              'old_value': iter_(value1, value1),
                              'new_value': value2,
                              'status': 'changed'}]

        return diff
    if formatter == plain:
        return plain(iter_(file1, file2))
    elif formatter == json:
        return json(iter_(file1, file2))
    else:
        return stylish(iter_(file1, file2))


def is_true_or_false_or_none(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value


def opening_files(path_file1, path_file2):
    if path_file1.endswith('yaml') or path_file1.endswith('yml'):
        with open(path_file1, 'r') as yml_file:
            file1 = yaml.safe_load(yml_file)
    else:
        file1 = jsn.load(open(path_file1))

    if path_file2.endswith('yaml') or path_file2.endswith('yml'):
        with open(path_file2, 'r') as yml_file:
            file2 = yaml.safe_load(yml_file)
    else:
        file2 = jsn.load(open(path_file2))
    return file1, file2
