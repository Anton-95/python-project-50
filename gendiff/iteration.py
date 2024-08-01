def iteration(file1, file2):

    keys = file1.keys() | file2.keys()
    sorted_keys = sorted(keys)

    diff = []

    for key in sorted_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff += [{'key': key,
                      'value': iteration(value1, value2),
                      'status': 'nested'}]

        else:
            if key not in file1:
                if isinstance(value2, dict):
                    diff += [{'key': key,
                              'value': iteration(value2, value2),
                              'status': 'added'}]
                else:
                    diff += [{'key': key,
                              'value': value2,
                              'status': 'added'}]

            elif key not in file2:
                if isinstance(value1, dict):
                    diff += [{'key': key,
                              'value': iteration(value1, value1),
                              'status': 'deleted'}]
                else:
                    diff += [{'key': key,
                              'value': value1,
                              'status': 'deleted'}]

            elif value1 != value2:
                if isinstance(value1, dict):
                    diff += [{'key': key,
                              'old_value': iteration(value1, value1),
                              'new_value': value2,
                              'status': 'changed'}]
                elif isinstance(value2, dict):
                    diff += [{'key': key,
                              'old_value': value1,
                              'new_value': iteration(value2, value2),
                              'status': 'changed'}]
                else:
                    diff += [{'key': key,
                              'old_value': value1,
                              'new_value': value2,
                              'status': 'changed'}]
            else:
                diff += [{'key': key,
                          'value': value1}]

    return diff
