import pytest
from gendiff import generate_diff


def read_result(path_file):
    with open(path_file, "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, formatter, result",
    [
        (
            "tests/fixtures/flat_file1.json",
            "tests/fixtures/flat_file2.yml",
            "stylish",
            "tests/fixtures/stylish_flat_string.txt",
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "stylish",
            "tests/fixtures/stylish_nested_string.txt",
        ),
        (
            "tests/fixtures/flat_file1.json",
            "tests/fixtures/flat_file2.yml",
            "plain",
            "tests/fixtures/plain_flat_string.txt",
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "plain",
            "tests/fixtures/plain_nested_string.txt",
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "json",
            "tests/fixtures/json_string.txt",
        ),
    ],
)
def test_generate_diff_formatters(file1, file2, formatter, result):
    assert generate_diff(file1, file2, formatter) == read_result(result)


def test_invalid_format_file():
    with pytest.raises(
        ValueError,
        match=("Unsupported file format. "
               "Expected '.yaml', '.yml' or '.json'."),
    ):
        generate_diff(
            "tests/fixtures/flat_file1.txt",
            "tests/fixtures/flat_file2.yml",
            "stylish"
        )


def test_invalid_formatter():
    with pytest.raises(
        ValueError,
        match=("Unsupported format. Expected 'stylish', 'plain' or 'json'"),
    ):
        generate_diff(
            "tests/fixtures/flat_file1.json",
            "tests/fixtures/flat_file2.yml",
            "nested"
        )
