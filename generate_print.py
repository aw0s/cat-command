#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from sys import exit


def generate_print(options, cwd: str) -> str:
    """Generates file content - line by line depending on specific option."""
    index = 1
    minus = 0

    five_spaces = "     "
    to_print = ""

    global path
    for file in options.files:
        if os.path.exists(file):
            path = file
        elif os.path.exists(f"{cwd}/{file}"):
            path = f"{cwd}/{file}"
        else:
            print(f"{file}: No such file or directory.")
            exit(0)

        with open(path, "r") as f:
            readl = f.readlines()

        if options.number:
            for line in readl:
                to_print += f"{five_spaces}{index}  {line}"

                index += 1
        elif options.number_notblank:
            for line in readl:
                line = line.replace("\n", "")

                if line:
                    to_print += f"{five_spaces}{index - minus}  {line}\n"
                else:
                    to_print += f"{line}\n"
                    minus += 1

                index += 1

            to_print = to_print.rstrip("\n")
        else:
            for line in readl:
                to_print += line

        if options.number_notblank:
            to_print += "\n"  # Because it's end of file.

    if options.A:
        to_print = to_print.replace("\t", "^I")

        to_print_split = to_print.split("\n")
        to_print_split = [f"{line}$\n" for line in to_print_split]

        to_print = "".join(to_print_split)
    else:
        if options.show_tabs:
            to_print = to_print.replace("\t", "^I")

        if options.show_ends:
            to_print_split = to_print.split("\n")
            to_print_split = [f"{line}$\n" for line in to_print_split]

            to_print = "".join(to_print_split)

    if options.squeeze_blank:
        empty_lines = 0
        to_print_split = to_print.split("\n")

        for index, line in enumerate(to_print_split):
            if not line or line == "\n":
                empty_lines += 1
            else:
                empty_lines = 0

            if empty_lines >= 2:
                to_print_split.pop(index)

        to_print = "\n".join(to_print_split)

    return to_print
