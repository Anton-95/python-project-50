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
            read_result("tests/fixtures/stylish_flat_string.txt"),
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "stylish",
            read_result("tests/fixtures/stylish_nested_string.txt"),
        ),
        (
            "tests/fixtures/flat_file1.json",
            "tests/fixtures/flat_file2.yml",
            "plain",
            read_result("tests/fixtures/plain_flat_string.txt"),
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "plain",
            read_result("tests/fixtures/plain_nested_string.txt"),
        ),
        (
            "tests/fixtures/nested_file3.json",
            "tests/fixtures/nested_file4.yml",
            "json",
            read_result("tests/fixtures/json_string.txt"),
        ),
    ],
)
def test_generate_diff_formatters(file1, file2, formatter, result):
    assert generate_diff(file1, file2, formatter) == result


@pytest.mark.parametrize(
    "file1, file2, formatter",
    [
        (
            "tests/fixtures/flat_file1.txt",
            "tests/fixtures/flat_file2.yml",
            "stylish",
        ),
    ]
)
def test_invalid_format_file(file1, file2, formatter):
    with pytest.raises(ValueError,
                       match=("Unsupported file format. "
                              "Expected '.yaml', '.yml' or '.json'.")):
        generate_diff(file1, file2, formatter)


@pytest.mark.parametrize(
    "file1, file2, formatter",
    [
        (
            "tests/fixtures/flat_file1.json",
            "tests/fixtures/flat_file2.yml",
            "nested",
        ),
    ],
)
def test_invalid_formatter(file1, file2, formatter):
    with pytest.raises(
        ValueError,
        match=("Unsupported format. Expected 'stylish', 'plain' or 'json'"),
    ):
        generate_diff(file1, file2, formatter)
