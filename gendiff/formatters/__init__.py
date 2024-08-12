from gendiff.formatters.json import gen_json_format
from gendiff.formatters.plain import gen_plain_format
from gendiff.formatters.stylish import gen_stylish_format


def get_formatter(formatter):
    """
    Returns a formatter function according to the given formatter

    Args:
        formatter (str): Formatter name

    Raises:
        ValueError: Unsupported formatter name
    """
    if formatter == "plain":
        return gen_plain_format
    elif formatter == "json":
        return gen_json_format
    elif formatter == "stylish":
        return gen_stylish_format
    else:
        raise ValueError("Unsupported format. "
                         "Expected 'stylish', 'plain' or 'json'")
