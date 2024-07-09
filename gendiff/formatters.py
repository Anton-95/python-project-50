def stylish(value, replacer=' ', spaces_count=4, depth=0):
    if not isinstance(value, dict):
        return value
    sorted_dict = dict(sorted(
        value.items(), key=lambda x: (x[0].strip(' -+'), x[0][1])))
    depth += spaces_count
    result_string = ''

    for key, item in sorted_dict.items():
        if str(key).startswith('+') or str(key).startswith('-'):
            result_string += f'{(depth - 2) * replacer}{key}: {stylish(
                item, replacer, spaces_count, depth)}\n'
        else:
            result_string += f'{depth * replacer}{key}: {stylish(
                item, replacer, spaces_count, depth)}\n'

    result = '{\n' + result_string + (replacer * (
        depth - spaces_count)) + '}\n'
    return result.strip('\n')
