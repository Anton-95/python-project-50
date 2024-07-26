from gendiff.gen_diff import generate_diff
import argparse


def input_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()

    if args.format == 'stylish':
        print(generate_diff(args.first_file, args.second_file,
                            formatter=args.format))

    elif args.format == 'plain':
        print(generate_diff(args.first_file,
                            args.second_file,
                            formatter=args.format))

    elif args.format == 'json':
        print(generate_diff(args.first_file,
                            args.second_file,
                            formatter=args.format))
