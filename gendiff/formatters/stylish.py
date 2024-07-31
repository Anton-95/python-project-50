def gen_nested_format(diff, replacer=' ', spaces_count=4, depth=0):
    depth += spaces_count
    result_string = ''

    for value in diff:

        if value.get('status') != 'nested':
            if value.get('status') == 'added':
                if isinstance(value['value'], list):
                    result_string += (
                        f'{(depth - 2) * replacer}+ '
                        f'{value['key']}: {gen_nested_format(value['value'],
                                                             replacer,
                                                             spaces_count,
                                                             depth)}\n')
                else:
                    value['value'] = to_str(value['value'])
                    result_string += (
                        f'{(depth - 2) * replacer}+ '
                        f'{value['key']}: {value['value']}\n')

            elif value.get('status') == 'deleted':
                if isinstance(value['value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['value'],
                                                           replacer,
                                                           spaces_count,
                                                           depth)}\n')
                else:
                    value['value'] = to_str(value['value'])
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: {value['value']}\n')

            elif value.get('status') is None:
                if isinstance(value['value'], list):
                    result_string += (f'{depth * replacer}'
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['value'],
                                                           replacer,
                                                           spaces_count,
                                                           depth)}\n')
                else:
                    value['value'] = to_str(value['value'])
                    result_string += (f'{depth * replacer}'
                                      f'{value['key']}: {value['value']}\n')

            elif value.get('status') == 'changed':
                if not isinstance(value['old_value'], list) and \
                   not isinstance(value['new_value'], list):
                    value['old_value'] = to_str(value['old_value'])
                    value['new_value'] = to_str(value['new_value'])
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: {value['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: {value['new_value']}\n')

                elif isinstance(value['old_value'], list) and \
                        not isinstance(value['new_value'], list):
                    value['new_value'] = to_str(value['new_value'])
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['old_value'],
                                         replacer,
                                         spaces_count,
                                         depth)}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: {value['new_value']}\n')

                elif not isinstance(value['old_value'], list) and \
                        isinstance(value['new_value'], list):
                    value['old_value'] = to_str(value['old_value'])
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: {value['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['new_value'],
                                         replacer,
                                         spaces_count,
                                         depth)}\n')

        if value.get('status') == 'nested':
            result_string += (f'{depth * replacer}'
                              f'{value['key']}: '
                              f'{gen_nested_format(value['value'],
                                 replacer,
                                 spaces_count,
                                 depth)}\n')

    result = '{\n' + result_string + (replacer * (depth - spaces_count)) + '}\n'
    return result.strip('\n')


def to_str(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
