import json


def gen_json_format(diff):
    result_string = ''
    for value in diff:
        result_string += f'{value}, '
    return json.dumps(result_string.strip(', '))
