def gen_plain_format(diff, path=''):
    result_string = ''
    if isinstance(diff, list):
        diff = sorted(diff, key=lambda x: x.get('key'))

    for value in diff:

        if value.get('children') is None:
            path += f'{value['key']}.'
            if value['status'] == 'added':
                result_string += (f"Property '{path.strip('.')}' "
                                  f"was added with value: "
                                  f"{is_bool_or_list(value['value'])}\n")
                path = path[0:-len(value['key']) - 1]
            elif value['status'] == 'deleted':
                result_string += f"Property '{path.strip('.')}' was removed\n"
                path = path[0:-len(value['key']) - 1]
            elif value['status'] == 'changed':
                result_string += (f"Property '{path.strip('.')}' was updated. "
                                  f"From {is_bool_or_list(value['old_value'])} "
                                  f"to {is_bool_or_list(value['new_value'])}\n")
                path = path[0:-len(value['key']) - 1]
            elif value['status'] == 'unchanged':
                path = path[0:-len(value['key']) - 1]

        else:
            path += f'{value['key']}.'
            if value['status'] == 'added':
                result_string += (f"Property '{path.strip('.')}' "
                                  f"was added with value: [complex value]")
            elif value['status'] == 'deleted':
                result_string += f"Property '{path.strip('.')}' was removed"
                path = path[0:-len(value.get('key')) - 1]
            result_string += f'{gen_plain_format(value.get('children'), path)}\n'
            path = path[0:-len(value.get('key')) - 1]

    return result_string.strip('\n')


def is_bool_or_list(value):
    if isinstance(value, list):
        return '[complex value]'
    elif value == 'true' or value == 'false' or value == 'null':
        return f'{value}'
    else:
        return f"'{value}'"
