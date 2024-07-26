from gendiff.formatters import format_selection
from gendiff.load_files import opening_files


def generate_diff(path_file1, path_file2, formatter='stylish'):
    file1, file2 = opening_files(path_file1), opening_files(path_file2)

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
    return format_selection(iter_(file1, file2), formatter)


def is_true_or_false_or_none(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
