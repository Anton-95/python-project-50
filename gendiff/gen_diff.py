from gendiff.formatters import get_formatter
from gendiff.parser import load_file
from gendiff.diff_builder import builder


def generate_diff(path_file1, path_file2, formatter='stylish'):
    file1, file2 = load_file(path_file1), load_file(path_file2)
    format = get_formatter(formatter)
    return format(builder(file1, file2))
