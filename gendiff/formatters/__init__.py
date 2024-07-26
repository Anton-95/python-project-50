from gendiff.formatters.plain import gen_plain_format as plain
from gendiff.formatters.stylish import gen_nested_format as stylish
from gendiff.formatters.json import gen_json_format as json


def format_selection(diff, formatter):
    if formatter == 'plain':
        return plain(diff)
    elif formatter == 'json':
        return json(diff)
    elif formatter == 'stylish':
        return stylish(diff)


__all__ = (
    'plain',
    'stylish',
    'json'
)
