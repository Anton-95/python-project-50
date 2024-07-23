from gendiff import generate_diff
import pytest


@pytest.fixture
def stylish_flat_string():
    with open('tests/fixtures/stylish_flat_string.txt',
              'r') as stylish_flat_string:
        content = stylish_flat_string.read()
        return content


@pytest.fixture
def stylish_nested_string():
    with open('tests/fixtures/stylish_nested_string.txt',
              'r')as stylish_nested_string:
        content = stylish_nested_string.read()
        return content


@pytest.fixture
def plain_flat_string():
    with open('tests/fixtures/plain_flat_string.txt',
              'r') as plain_flat_string:
        content = plain_flat_string.read()
        return content


@pytest.fixture
def plain_nested_string():
    with open('tests/fixtures/plain_nested_string.txt',
              'r') as plain_nested_string:
        content = plain_nested_string.read()
        return content


@pytest.fixture
def json_string():
    with open('tests/fixtures/json_string.txt',
              'r') as json_string:
        content = json_string.read()
        return content


def test_generate_diff_flat_stylish(stylish_flat_string):
    file1 = 'tests/fixtures/flat_file1.json'
    file2 = 'tests/fixtures/flat_file2.json'
    assert generate_diff(file1, file2, 'stylish') == stylish_flat_string

    file1 = 'tests/fixtures/flat_file1.yml'
    file2 = 'tests/fixtures/flat_file2.yml'
    assert generate_diff(file1, file2, 'stylish') == stylish_flat_string


def test_generate_diff_nested_stylish(stylish_nested_string):
    file1 = 'tests/fixtures/nested_file3.json'
    file2 = 'tests/fixtures/nested_file4.json'
    assert generate_diff(file1, file2, 'stylish') == stylish_nested_string

    file1 = 'tests/fixtures/nested_file3.yml'
    file2 = 'tests/fixtures/nested_file4.yml'
    assert generate_diff(file1, file2, 'stylish') == stylish_nested_string


def test_generate_diff_flat_plain(plain_flat_string):
    file1 = 'tests/fixtures/flat_file1.json'
    file2 = 'tests/fixtures/flat_file2.json'
    assert generate_diff(file1, file2, formatter='plain') == plain_flat_string

    file1 = 'tests/fixtures/flat_file1.yml'
    file2 = 'tests/fixtures/flat_file2.yml'
    assert generate_diff(file1, file2, formatter='plain') == plain_flat_string


def test_generate_diff_nested_plain(plain_nested_string):
    file1 = 'tests/fixtures/nested_file3.json'
    file2 = 'tests/fixtures/nested_file4.json'
    assert generate_diff(file1, file2, formatter='plain') == plain_nested_string

    file1 = 'tests/fixtures/nested_file3.yml'
    file2 = 'tests/fixtures/nested_file4.yml'
    assert generate_diff(file1, file2, formatter='plain') == plain_nested_string


def test_generate_diff_json(json_string):
    file1 = 'tests/fixtures/nested_file3.json'
    file2 = 'tests/fixtures/nested_file4.json'
    assert generate_diff(file1, file2, formatter='json') == json_string
