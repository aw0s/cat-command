#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Args:
    def __init__(self, args, readl: list):
        self.args = args
        self.readl = readl

        self.generated_lines = ""

    def generate_lines(self) -> str:
        flags_dict = {
            self.args.number: self.n_option,
            # self.args.number_notblank: self.b_option,
        }

        generated_lines = flags_dict[]


    def n_option(self):
        for index, line in enumerate(self.readl):
            self.generated_lines += f"\t{index} {line}\n"

        return generate_lines

    def __str__(self) -> str:
        return self.generated_lines
