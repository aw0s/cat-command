#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import exit


def generate_print(options, cwd: str) -> str:
    """Generates file content - line by line depending on specific option."""
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

        to_print = ""

        if options.number:
            for index, line in enumerate(readl, start=1):
                to_print += f"     {index}  {line}"
        elif options.number_notblank:
            minus = 0
            for index, line in enumerate(readl, start=1):
                line = line.replace("\n", "")

                if line:
                    to_print += f"     {index - minus}  {line}\n"
                else:
                    to_print += f"{line}\n"
                    minus += 1

            to_print = to_print[:-3]
        else:
            for line in readl:
                to_print += line

        if options.A:
            to_print = to_print.replace("\t", "^I")

            to_print_split = to_print.split("\n")
            to_print_split = [f"{line}$\n" for line in to_print_split]

            to_print = "".join(to_print_split)
        else:
            if options.T:
                pass
            # if options.

        return to_print
