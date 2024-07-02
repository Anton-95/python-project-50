from gendiff import generate_diff
import pytest


@pytest.fixture
def result_json_string():
    with open('tests/fixtures/json_string.txt', 'r') as json_string:
        content = json_string.read()
        return content


def test_generate_diff(result_json_string):

    file1 = 'gendiff/file1.json'
    file2 = 'gendiff/file2.json'

    assert generate_diff(file1, file2) == result_json_string
