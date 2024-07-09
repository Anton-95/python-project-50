from gendiff import generate_diff
import pytest


@pytest.fixture
def result_json_string():
    with open('tests/fixtures/result_flat_string.txt', 'r') as json_string:
        content = json_string.read()
        return content


@pytest.fixture
def result_nested_json_string():
    with open('tests/fixtures/result_nested_string.txt',
              'r')as json_nested_string:
        content = json_nested_string.read()
        return content


def test_generate_diff_primitive_json(result_json_string):
    file1 = 'tests/fixtures/flat_file1.json'
    file2 = 'tests/fixtures/flat_file2.json'
    assert generate_diff(file1, file2) == result_json_string


def test_genetrate_diff_primitive_yaml(result_json_string):
    file1 = 'tests/fixtures/flat_file1.yml'
    file2 = 'tests/fixtures/flat_file2.yml'
    assert generate_diff(file1, file2) == result_json_string


def test_generate_diff_nested_json(result_nested_json_string):
    file1 = 'tests/fixtures/nested_file3.json'
    file2 = 'tests/fixtures/nested_file4.json'
    assert generate_diff(file1, file2) == result_nested_json_string


def test_generate_diff_nested_yaml(result_nested_json_string):
    file1 = 'tests/fixtures/nested_file3.yml'
    file2 = 'tests/fixtures/nested_file4.yml'
    assert generate_diff(file1, file2) == result_nested_json_string
