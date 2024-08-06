from gendiff.formatters.plain import gen_plain_format as plain
from gendiff.formatters.stylish import gen_nested_format as stylish
from gendiff.formatters.json import gen_json_format as json


def get_formatter(formatter):
    if formatter == 'plain':
        return plain
    elif formatter == 'json':
        return json
    elif formatter == 'stylish':
        return stylish
