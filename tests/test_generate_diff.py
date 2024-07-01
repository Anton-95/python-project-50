from gendiff import generate_diff

result_string = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff():

    file1 = 'gendiff/file1.json'
    file2 = 'gendiff/file2.json'

    assert generate_diff(file1, file2) == result_string
