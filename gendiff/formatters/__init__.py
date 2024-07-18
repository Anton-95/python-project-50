from gendiff.formatters.plain import gen_plain_format as plain
from gendiff.formatters.stylish import gen_nested_format as stylish
from gendiff.formatters.json import gen_json_format as json

__all__ = (
    'plain',
    'stylish',
    'json'
)
