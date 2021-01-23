#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument(nargs='*', dest='files')
    parser.add_argument('-n', '--number', action='store_true')
    parser.add_argument('-b', '--number_notblank', action='store_true')
    parser.add_argument('-E', action='store_true')

    args = parser.parse_args()

    return args


def read_print(path: str, options):
    """Prints file content - line by line."""
    with open(path, 'r') as f:
        readl = f.readlines()

    if options.number_notblank:
        on_minus = 0
        for index, line in enumerate(readl, start=1):
            line = line.replace('\n', '')
            if line:
                print(f"     {index - on_minus}  {line}")
            else:
                print()
                on_minus += 1

    elif options.number:
        for index, line in enumerate(readl, start=1):
            line = line.replace('\n', '')
            print(f"     {index}  {line}")



def main():
    args = create_parser()

    cwd = os.getcwd()

    if args.files:
        for file_path in args.files:
            if os.path.exists(file_path) and os.path.exists(f'{cwd}/{file_path}'):
                try:
                    read_print(path=file_path, options=args)
                except FileNotFoundError:
                    read_print(path=f'{cwd}/{file_path}', options=args)
            else:
                print(f"{file_path}: No such file or directory.")
    else:
        while True:
            inp = input()
            print(inp)


if __name__ == '__main__':
    main()
