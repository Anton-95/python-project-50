from gendiff.formatters.plain import gen_plain_format
from gendiff.formatters.stylish import gen_nested_format
from gendiff.formatters.json import gen_json_format


def get_formatter(formatter):
    if formatter == 'plain':
        return gen_plain_format
    elif formatter == 'json':
        return gen_json_format
    elif formatter == 'stylish':
        return gen_nested_format
