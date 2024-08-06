from gendiff.formatters import format_selection
from gendiff.parser import load_file
from gendiff.diff_builder import iteration


def generate_diff(path_file1, path_file2, formatter='stylish'):
    file1, file2 = load_file(path_file1), load_file(path_file2)
    return format_selection(iteration(file1, file2), formatter)
