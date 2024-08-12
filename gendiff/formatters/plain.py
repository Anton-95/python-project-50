def gen_plain_format(diff, path=''):
    """
    Returns a string in plain format

    Args:
        diff (list): List with differences
        path (str, optional): Path to current element. Defaults to ''.
    """
    result_string = ''

    for value in diff:

        path += f'{value["key"]}.'
        if value.get('status') == 'nested':
            result_string += f'{gen_plain_format(value.get('value'), path)}\n'

        elif value.get('status') == 'added':
            result_string += (f"Property '{path.strip('.')}' "
                              f"was added with value: "
                              f"{to_str(value['value'])}\n")

        elif value.get('status') == 'deleted':
            result_string += f"Property '{path.strip('.')}' was removed\n"

        elif value.get('status') == 'changed':
            result_string += (f"Property '{path.strip('.')}' was updated. "
                              f"From {to_str(value['old_value'])} "
                              f"to {to_str(value['new_value'])}\n")

        path = path[0:-len(value['key']) - 1]

    return result_string.strip('\n')


def to_str(value):
    """
    Converts value to string in plain format

    Args:
        value (bool, int, list, dict): Value to convert
    """
    if isinstance(value, list) or isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"
