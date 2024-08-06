def gen_plain_format(diff, path=''):
    result_string = ''

    def del_last_path(path, del_path):
        return path[0:-len(del_path['key']) - 1]

    for value in diff:

        if value.get('status') != 'nested':
            path += f'{value['key']}.'

            if value.get('status') is None:
                path = del_last_path(path, value)

            elif value['status'] == 'added':
                result_string += (f"Property '{path.strip('.')}' "
                                  f"was added with value: "
                                  f"{to_str(value['value'])}\n")
                path = del_last_path(path, value)

            elif value['status'] == 'deleted':
                result_string += f"Property '{path.strip('.')}' was removed\n"
                path = del_last_path(path, value)

            elif value['status'] == 'changed':
                result_string += (f"Property '{path.strip('.')}' was updated. "
                                  f"From {to_str(value['old_value'])} "
                                  f"to {to_str(value['new_value'])}\n")
                path = del_last_path(path, value)

        elif value.get('status') == 'nested':
            path += f'{value['key']}.'
            result_string += f'{gen_plain_format(value.get('value'), path)}\n'
            path = del_last_path(path, value)

    return result_string.strip('\n')


def to_str(value):
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
