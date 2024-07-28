from gendiff.formatters import format_selection
from gendiff.load_files import opening_files
from gendiff.iteration import iteration


def generate_diff(path_file1, path_file2, formatter='stylish'):
    file1, file2 = opening_files(path_file1), opening_files(path_file2)
    return format_selection(iteration(file1, file2), formatter)
