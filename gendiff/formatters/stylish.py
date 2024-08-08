def gen_nested_format(diff, sep=' ', sep_count=4, depth=0):
    depth += sep_count
    result_string = ''

    for value in diff:

        if value.get('status') != 'nested':
            if value.get('status') == 'added':
                result_string += (f'{(depth - 2) * sep}+ '
                                  f'{value['key']}: '
                                  f'{to_str(value['value'],
                                            depth,
                                            sep_count,
                                            sep)}\n')

            elif value.get('status') == 'deleted':
                result_string += (f'{(depth - 2) * sep}- '
                                  f'{value['key']}: '
                                  f'{to_str(value['value'],
                                            depth,
                                            sep_count,
                                            sep)}\n')

            elif value.get('status') is None:
                result_string += (f'{depth * sep}'
                                  f'{value['key']}: '
                                  f'{to_str(value['value'],
                                            depth,
                                            sep_count,
                                            sep)}\n')

            elif value.get('status') == 'changed':
                result_string += (f'{(depth - 2) * sep}- '
                                  f'{value['key']}: {to_str(value['old_value'],
                                                            depth,
                                                            sep_count,
                                                            sep)}\n')
                result_string += (f'{(depth - 2) * sep}+ '
                                  f'{value['key']}: {to_str(value['new_value'],
                                                            depth,
                                                            sep_count,
                                                            sep)}\n')

        if value.get('status') == 'nested':
            result_string += (f'{depth * sep}'
                              f'{value['key']}: '
                              f'{gen_nested_format(value['value'],
                                 sep,
                                 sep_count,
                                 depth)}\n')

    result = '{\n' + result_string + (sep * (depth - sep_count)) + '}\n'
    return result.strip('\n')


def dict_to_str(data, depth, sep_count, sep):
    depth += sep_count
    result_string = ''

    for key, value in data.items():
        if not isinstance(value, dict):
            result_string += (f'{depth * sep}'
                              f'{key}: {value}\n')
        elif isinstance(value, dict):
            result_string += (f'{depth * sep}'
                              f'{key}: {dict_to_str(value,
                                                    depth,
                                                    sep_count,
                                                    sep)}\n')

    result = '{\n' + result_string + (sep * (depth - sep_count)) + '}\n'
    return result.strip('\n')


def to_str(value, depth, sep_count, sep):
    if isinstance(value, dict):
        return dict_to_str(value, depth, sep_count, sep)
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
