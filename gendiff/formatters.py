def sorting_dict(diff_dict):
    sorted_dict = dict(sorted(
        diff_dict.items(), key=lambda x: (x[0].strip(' -+'), x[0][1])))
    for key, value in sorted_dict.items():
        if not isinstance(value, dict):
            sorted_dict[key] = value
        else:
            sorted_dict[key] = sorting_dict(value)
    return sorted_dict


def stylish(diff, replacer=' ', spaces_count=4, depth=0):
    depth += spaces_count
    result_string = ''
    if isinstance(diff, list):
        diff = sorted(diff, key=lambda x: x.get('key'))

    for item in diff:

        if item.get('children') is None:
            if item.get('status') == 'added':
                result_string += (
                    f'{(depth - 2) * replacer}+ '
                    f'{item['key']}: {item['value']}\n')
            elif item.get('status') == 'deleted':
                result_string += (f'{(depth - 2) * replacer}- '
                                  f'{item['key']}: {item['value']}\n')
            elif item.get('status') == 'unchanged':
                result_string += (f'{depth * replacer}'
                                  f'{item['key']}: {item['value']}\n')
            elif item.get('status') == 'changed':
                if not isinstance(item['old_value'], list) and \
                   not isinstance(item['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{item['key']}: {item['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{item['key']}: {item['new_value']}\n')
                elif isinstance(item['old_value'], list) and \
                        not isinstance(item['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{item['key']}: '
                                      f'{stylish(item['old_value'],
                                                 replacer,
                                                 spaces_count,
                                                 depth)}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{item['key']}: {item['new_value']}\n')
                elif not isinstance(item['old_value'], list) and \
                        isinstance(item['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{item['key']}: {item['old_value']}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{item['key']}: '
                                      f'{stylish(item['new_value'],
                                                 replacer,
                                                 spaces_count,
                                                 depth)}\n')
                elif isinstance(item['old_value'], list) and \
                        not isinstance(item['new_value'], list):
                    result_string += (f'{(depth - 2) * replacer}- '
                                      f'{item['key']}: '
                                      f'{stylish(item['old_value'],
                                                 replacer,
                                                 spaces_count,
                                                 depth)}\n')
                    result_string += (f'{(depth - 2) * replacer}+ '
                                      f'{item['key']}: '
                                      f'{stylish(item['new_value'],
                                                 replacer,
                                                 spaces_count,
                                                 depth)}\n')

        elif item['children'] is not None:
            if item.get('status') == 'added':
                result_string += (f'{(depth - 2) * replacer}+ '
                                  f'{item['key']}: '
                                  f'{stylish(item['children'],
                                             replacer,
                                             spaces_count,
                                             depth)}\n')
            elif item.get('status') == 'deleted':
                result_string += (f'{(depth - 2) * replacer}- '
                                  f'{item['key']}: '
                                  f'{stylish(item['children'],
                                             replacer,
                                             spaces_count,
                                             depth)}\n')
            elif item.get('status') == 'unchanged':
                result_string += (f'{depth * replacer}'
                                  f'{item['key']}: '
                                  f'{stylish(item['children'],
                                             replacer,
                                             spaces_count,
                                             depth)}\n')

    result = '{\n' + result_string + (replacer * (depth - spaces_count)) + '}\n'
    return result.strip('\n')
