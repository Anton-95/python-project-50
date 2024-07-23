import json


def sorting_diff(diff):
    if isinstance(diff, list):
        return sorted([sorting_diff(elem) for elem in diff],
                      key=lambda x: x['key'])
    if isinstance(diff, dict):
        return {k: sorting_diff(v) for k, v in sorted(diff.items())}
    return diff


def gen_json_format(diff):
    sorted_diff = sorting_diff(diff)
    result_string = ''
    for value in sorted_diff:
        result_string += f'{value}, '
    return json.dumps(result_string.strip(', '))
