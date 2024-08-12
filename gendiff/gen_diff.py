from gendiff.formatters import get_formatter
from gendiff.parser import load_file
from gendiff.diff_builder import builder


def generate_diff(path_file1, path_file2, formatter='stylish'):
    """
    Generates diff between two files and returns it as a string in the given
    formatter (plain, stylish or json)

    Args:
        path_file1 (str): Path to first file
        path_file2 (str): Path to second file
        formatter (str, optional): Formatter name. Defaults to 'stylish'.
    """
    file1, file2 = load_file(path_file1), load_file(path_file2)
    formatter = get_formatter(formatter)
    return formatter(builder(file1, file2))
