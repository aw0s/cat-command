#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument(nargs='*', dest='files')
    parser.add_argument('-n', '--number', action='store_true')
    parser.add_argument('-b', '--number_notblank', action='store_true')
    parser.add_argument('-A', '-show_all', action='store_true')
    parser.add_argument('-E', action='store_true')  # shows "$" at end of each file
    parser.add_argument('-T', action='store_true')  # shows "^I" instead of tabs

    args = parser.parse_args()

    return args


def read_print(path: str, options) -> str:
    """Prints file content - line by line depending on specific option."""
    with open(path, 'r') as f:
        readl = f.readlines()

    to_print = ""

    if options.number_notblank:
        minus = 0
        for index, line in enumerate(readl, start=1):
            line = line.replace('\n', '')

            if line:
                to_print += f"     {index - minus}  {line}\n"
            else:
                to_print += f"{line}\n"
                minus += 1
    elif options.number:
        for index, line in enumerate(readl, start=1):
            # line = line.replace('\n', '')

            to_print += f"     {index}  {line}"
    else:
        for line in readl:
            # line = line.replace('\n', '')

            to_print += line

    if options.A:
        to_print = to_print.replace('\t', '^I')

        to_print_split = to_print.split('\n')
        to_print_split = [f"{line}$\n" for line in to_print_split]

        to_print = "".join(to_print_split)
    else:
        if options.T:
            pass
        # elif options.

    return to_print[:-3]


def main():
    args = create_parser()
    cwd = os.getcwd()

    if args.files:
        for file_path in args.files:
            if os.path.exists(file_path) and os.path.exists(f'{cwd}/{file_path}'):
                try:
                    print(read_print(path=file_path, options=args))
                except FileNotFoundError:
                    print(read_print(path=f'{cwd}/{file_path}', options=args))
            else:
                print(f"{file_path}: No such file or directory.")
    else:
        while True:
            inp = input()
            print(inp)


if __name__ == '__main__':
    main()
