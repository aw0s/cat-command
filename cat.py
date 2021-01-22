#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
import os
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument(nargs='*', dest='files')
    args = parser.parse_args()

    cwd = os.getcwd()

    for file in args.files:
        if os.path.exists(file) and os.path.exists(f'{cwd}/{file}'):
            try:
                with open(f'{file}', 'r') as f:
                    readl = f.readlines()

                for line in readl:
                    print(line.replace('\n', ''))
            except FileNotFoundError:
                with open(f'{cwd}/{file}', 'r') as f:
                    readl = f.readlines()

                for line in readl:
                    print(line)
        else:
            print(f"{file}: No such file or directory.")
            exit(0)


if __name__ == '__main__':
    main()
