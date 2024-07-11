from gendiff.formatters import stylish
import json
import yaml


def generate_diff(path_file1, path_file2, formatter=stylish):
    file1, file2 = opening_files(path_file1, path_file2)

    def iter_(file1, file2):

        keys = file1.keys() | file2.keys()
        diff_dict = {}

        for key in keys:
            value1 = is_true_or_false_or_none(file1.get(key))
            value2 = is_true_or_false_or_none(file2.get(key))
            
            if not isinstance(value1, dict) and not isinstance(value2, dict):
                if key not in file1:
                    diff_dict[key] = (value2, 'added')
                elif key not in file2:
                    diff_dict[key] = (value1, 'deleted')
                elif value1 == value2:
                    diff_dict[key] = (value1, 'unchanged')
                else:
                    diff_dict[key] = (value1, value2, 'changed')
            elif isinstance(value1, dict) and isinstance(value2, dict):
                diff_dict[key] = iter_(value1, value2)
            elif not isinstance(value1, dict) and isinstance(value2, dict) and file1.get(key) is None:
                diff_dict[key] = (value2, 'added')
            elif isinstance(value1, dict) and not isinstance(value2, dict) and file2.get(key) is not None:
                diff_dict[key] = (value1, value2, 'changed')
            else:
                diff_dict[key] = (value1, 'deleted')
            
        return diff_dict
    return formatter(iter_(file1, file2))


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
        file1 = json.load(open(path_file1))

    if path_file2.endswith('yaml') or path_file2.endswith('yml'):
        with open(path_file2, 'r') as yml_file:
            file2 = yaml.safe_load(yml_file)
    else:
        file2 = json.load(open(path_file2))
    return file1, file2

# Первый вариант внутреннего представления
        # diff_dict = {}

        # for key, value in file1.items():
        #     value = is_true_or_false_or_none(value)
        #     if not isinstance(value, dict):
        #         if file2.get(key) is None:
        #             diff_dict[f'- {key}'] = value
        #         elif file2.get(key) == file1[key]:
        #             diff_dict[f'{key}'] = value
        #         elif file2.get(key) != file1[key]:
        #             diff_dict[f'- {key}'] = value
        #             diff_dict[f'+ {key}'] = file2[key]
        #     elif isinstance(value, dict):
        #         if isinstance(file2.get(key), dict):
        #             diff_dict[key] = iter_(value, file2.get(key))
        #         elif not isinstance(file2.get(key), dict):
        #             diff_dict[f'- {key}'] = iter_(value, value)

        # for key, value in file2.items():
        #     value = is_true_or_false_or_none(value)
        #     if not isinstance(value, dict):
        #         if file1.get(key) is None or file1.get(key) != value:
        #             diff_dict[f'+ {key}'] = value
        #     elif isinstance(value, dict):
        #         if isinstance(file1.get(key), dict):
        #             if file1.get(key) is None:
        #                 diff_dict[f'+ {key}'] = iter_(value, file1.get(key))
        #         elif not isinstance(file1.get(key), dict):
        #             diff_dict[f'+ {key}'] = iter_(value, value)
