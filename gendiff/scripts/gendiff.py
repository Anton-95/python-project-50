#!usr/bin/env python3
from gendiff import parse_arguments, generate_diff


def main():
    args = parse_arguments()
    print(generate_diff(args.first_file,
                        args.second_file,
                        formatter=args.format))


if __name__ == '__main__':
    main()
