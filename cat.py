#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from argparse import ArgumentParser

from generate_print import generate_print


def create_parser():
    """Initializes argument parser and required arguments.."""
    parser = ArgumentParser()

    parser.add_argument(nargs="*", dest="files")
    parser.add_argument("-n", "--number", action="store_true")
    parser.add_argument("-b", "--number_notblank", action="store_true")
    parser.add_argument("-s", "--squeeze_blank", action="store_true")
    parser.add_argument("-A", "-show_all", action="store_true")
    parser.add_argument(
        "-E", "--show_ends", action="store_true"
    )  # shows "$" at end of each file
    parser.add_argument(
        "-T", "--show_tabs", action="store_true"
    )  # shows "^I" instead of tabs

    args = parser.parse_args()

    return args


def main():
    args = create_parser()
    cwd = os.getcwd()

    if args.files:
        generated = generate_print(options=args, cwd=cwd)
        print(generated)
    else:
        while True:
            inp = input()
            print(inp)


if __name__ == "__main__":
    main()
