def gen_nested_format(diff, replacer=' ', spaces_count=4, depth=0):
    depth += spaces_count
    result_string = ''
    if isinstance(diff, list):
        diff = sorted(diff, key=lambda x: x.get('key'))

    for value in diff:

        if value.get('children') is None:
            if value.get('status') == 'added':
                result_string += (
                    f'{(depth - 2) * replacer}+ '
                    f'{value['key']}: {value['value']}\n')
            elif value.get('status') == 'deleted':
                result_string += (f'{(depth - 2) * replacer}- '
                                  f'{value['key']}: {value['value']}\n')
            elif value.get('status') == 'unchanged':
                result_string += (f'{depth * replacer}'
                                  f'{value['key']}: {value['value']}\n')
            elif value.get('status') == 'changed':
                if not isinstance(value['old_value'], list) and \
                   not isinstance(value['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: {value['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: {value['new_value']}\n')
                elif isinstance(value['old_value'], list) and \
                        not isinstance(value['new_value'], list):
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
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: {value['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['new_value'],
                                         replacer,
                                         spaces_count,
                                         depth)}\n')
                elif isinstance(value['old_value'], list) and \
                        not isinstance(value['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['old_value'],
                                         replacer,
                                         spaces_count,
                                         depth)}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{value['key']}: '
                                      f'{gen_nested_format(value['new_value'],
                                         replacer,
                                         spaces_count,
                                         depth)}\n')

        elif value['children'] is not None:
            if value.get('status') == 'added':
                result_string += (f'{(depth - 2) * replacer}+ '
                                  f'{value['key']}: '
                                  f'{gen_nested_format(value['children'],
                                     replacer,
                                     spaces_count,
                                     depth)}\n')
            elif value.get('status') == 'deleted':
                result_string += (f'{(depth - 2) * replacer}- '
                                  f'{value['key']}: '
                                  f'{gen_nested_format(value['children'],
                                     replacer,
                                     spaces_count,
                                     depth)}\n')
            elif value.get('status') == 'unchanged':
                result_string += (f'{depth * replacer}'
                                  f'{value['key']}: '
                                  f'{gen_nested_format(value['children'],
                                     replacer,
                                     spaces_count,
                                     depth)}\n')

    result = '{\n' + result_string + (replacer * (depth - spaces_count)) + '}\n'
    return result.strip('\n')
