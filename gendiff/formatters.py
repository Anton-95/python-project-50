def is_true_or_false_or_none(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value


def sorting_dict(diff_dict):
    sorted_dict = dict(sorted(
        diff_dict.items(), key=lambda x: (x[0].strip(' -+'), x[0][1])))
    for key, value in sorted_dict.items():
        if not isinstance(value, dict):
            sorted_dict[key] = value
        else:
            sorted_dict[key] = sorting_dict(value)
    return sorted_dict


def stylish(value, replacer=' ', spaces_count=4, depth=0):
    if not isinstance(value, dict):
        return value
    sorted_dict = sorting_dict(value)
    depth += spaces_count
    result_string = ''

    for key, item in sorted_dict.items():
        if isinstance(item, dict):
            result_string += f'{depth * replacer}{key}: {stylish(
                item, replacer, spaces_count, depth)}\n'

        elif not isinstance(item, dict) and not isinstance(item, tuple):
            result_string += f'{depth * replacer}{key}: {stylish(
                item, replacer, spaces_count, depth)}\n'

        elif isinstance(item, tuple):

            if item[-1] == 'added' and isinstance(item[0], dict):
                result_string += f'{(depth - 2) * replacer}+ {key}: {stylish(
                    item[0], replacer, spaces_count, depth)}\n'
            elif item[-1] == 'added' and not isinstance(item[0], dict):
                result_string += f'{(depth - 2) * replacer}+ {key}: {item[0]}\n'

            elif item[-1] == 'deleted' and isinstance(item[0], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {stylish(
                    item[0], replacer, spaces_count, depth)}\n'
            elif item[-1] == 'deleted' and not isinstance(item[0], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {item[0]}\n'

            elif item[-1] == 'unchanged' and isinstance(item[0], dict):
                result_string += f'{depth * replacer}{key}: {stylish(
                    item[0], replacer, spaces_count, depth)}\n'
            elif item[-1] == 'unchanged' and not isinstance(item[0], dict):
                result_string += f'{depth * replacer}{key}: {item[0]}\n'

            elif item[-1] == 'changed' and isinstance(item[0], dict) and isinstance(item[1], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {stylish(
                    item[0], replacer, spaces_count, depth)}\n'
                result_string += f'{(depth - 2) * replacer}+ {key}: {stylish(
                    item[1], replacer, spaces_count, depth)}\n'
            elif item[-1] == 'changed' and not isinstance(item[0], dict) and not isinstance(item[1], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {item[0]}\n'
                result_string += f'{(depth - 2) * replacer}+ {key}: {item[1]}\n'
            elif item[-1] == 'changed' and isinstance(item[0], dict) and not isinstance(item[1], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {stylish(
                    item[0], replacer, spaces_count, depth)}\n'
                result_string += f'{(depth - 2) * replacer}+ {key}: {item[1]}\n'
            elif item[-1] == 'changed' and not isinstance(item[0], dict) and isinstance(item[1], dict):
                result_string += f'{(depth - 2) * replacer}- {key}: {item[0]}\n'
                result_string += f'{(depth - 2) * replacer}+ {key}: {stylish(
                    item[1], replacer, spaces_count, depth)}\n'

    result = '{\n' + result_string + (replacer * (
        depth - spaces_count)) + '}\n'
    return result.strip('\n')

# stylish для первого варианта внутреннего представления дифа
    # for key, item in sorted_dict.items():
    #     if str(key).startswith('+') or str(key).startswith('-'):
    #         result_string += f'{(depth - 2) * replacer}{key}: {stylish(
    #             item, replacer, spaces_count, depth)}\n'
    #     else:
    #         result_string += f'{depth * replacer}{key}: {stylish(
    #             item, replacer, spaces_count, depth)}\n'

# def plain(value):
#     if not isinstance(value, dict):
#         return value
#     sorted_dict = sorting_dict(value)
    
#     for key, item in sorted_dict.items():
#         if isinstance(item, tuple):
#             if item[-1] == 'added':
                