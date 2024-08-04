def gen_plain_format(diff, path=''):
    result_string = ''

    for value in diff:

        if value.get('status') != 'nested':
            path += f'{value['key']}.'

            if value.get('status') is None:
                path = path[0:-len(value['key']) - 1]

            elif value['status'] == 'added':
                result_string += (f"Property '{path.strip('.')}' "
                                  f"was added with value: "
                                  f"{to_str(value['value'])}\n")
                path = path[0:-len(value['key']) - 1]

            elif value['status'] == 'deleted':
                result_string += f"Property '{path.strip('.')}' was removed\n"
                path = path[0:-len(value['key']) - 1]

            elif value['status'] == 'changed':
                result_string += (f"Property '{path.strip('.')}' was updated. "
                                  f"From {to_str(value['old_value'])} "
                                  f"to {to_str(value['new_value'])}\n")
                path = path[0:-len(value['key']) - 1]

        elif value.get('status') == 'nested':
            path += f'{value['key']}.'

            if value['status'] == 'added':
                result_string += (f"Property '{path.strip('.')}' "
                                  f"was added with value: [complex value]")

            elif value['status'] == 'deleted':
                result_string += f"Property '{path.strip('.')}' was removed"
                path = path[0:-len(value.get('key')) - 1]
            result_string += (f'{gen_plain_format(value.get('value'),
                              path)}\n')
            path = path[0:-len(value.get('key')) - 1]

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
