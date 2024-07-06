from gendiff.generate_diff import opened_files, is_true_or_false
from gendiff.generate_diff import make_sorted_string


def generate_diff(path_file1, path_file2):
    file1, file2 = opened_files(path_file1, path_file2)
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

    return make_sorted_string(result_dict)
