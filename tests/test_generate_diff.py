from gendiff import generate_diff
import pytest


def read_result(path_file):
    with open(path_file, 'r') as file:
        return file.read()


nested_file1 = 'tests/fixtures/nested_file3.json'
nested_file2 = 'tests/fixtures/nested_file4.yml'
flat_file1 = 'tests/fixtures/flat_file1.json'
flat_file2 = 'tests/fixtures/flat_file2.yml'
stylish_flat_string = 'tests/fixtures/stylish_flat_string.txt'
stylish_nested_string = 'tests/fixtures/stylish_nested_string.txt'
plain_flat_string = 'tests/fixtures/plain_flat_string.txt'
plain_nested_string = 'tests/fixtures/plain_nested_string.txt'
json_string = 'tests/fixtures/json_string.txt'


@pytest.mark.parametrize('file1, file2, formatter, result', [
    (flat_file1, flat_file2, 'stylish', read_result(stylish_flat_string)),
    (nested_file1, nested_file2, 'stylish', read_result(stylish_nested_string)),
    (flat_file1, flat_file2, 'plain', read_result(plain_flat_string)),
    (nested_file1, nested_file2, 'plain', read_result(plain_nested_string)),
    (nested_file1, nested_file2, 'json', read_result(json_string))
])
def test_generate_diff_flat_stylish(file1, file2, formatter, result):
    assert generate_diff(file1, file2, formatter) == result
