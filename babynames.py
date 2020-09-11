#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__author__ = "Jalal Belsifar, with help from JT, Kevin"

"""
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    with open(filename, 'r') as f:
        x = f.read()
        name_dict = {}
        names.append(re.findall(r'Popularity\sin\s(\d\d\d\d)', x)[0])
        data = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', x)
        for rank, boy_name, girl_name in data:
            if boy_name not in name_dict:
                name_dict[boy_name] = rank
            if girl_name not in name_dict:
                name_dict[girl_name] = rank
        for name in sorted(name_dict.keys()):
            names.append(f"{name} {name_dict[name]}")
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    create_summary = ns.summaryfile

    for file in file_list:
        result = extract_names(file)
        text = '\n'.join(result)
        if not create_summary:
            print(text)
        else:
            with open(file + ".summary", "w") as f:
                f.write(text)


if __name__ == '__main__':
    main(sys.argv[1:])
