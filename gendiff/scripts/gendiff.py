from gendiff.formatters import stylish
from gendiff.gen_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.first_file, args.second_file)

    print(generate_diff(args.first_file, args.second_file, formatter=stylish))


if __name__ == '__main__':
    main()
