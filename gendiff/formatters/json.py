import json


def gen_json_format(diff):
    if isinstance(diff, list):
        return sorted([gen_json_format(elem) for elem in diff],
                      key=lambda x: x['key'])
    if isinstance(diff, dict):
        return {k: gen_json_format(v) for k, v in sorted(diff.items())}
    return json.dumps(diff)
