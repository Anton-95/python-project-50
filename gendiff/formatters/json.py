import json


def gen_json_format(diff):
    """
    Returns a string in JSON format

    Args:
        diff (list): List with differences
    """
    return json.dumps(diff)
