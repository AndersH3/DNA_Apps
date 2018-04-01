#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

# Use only with files in ftdna format
# you can reformat your data with [https://ytree.morleydna.com/extractFromAutosomal]
# just copy and paste the data from the last step into a file.
# But do not hand edit the data.
# If you want to manually add some snps add them into a separate file eg extra.txt.
# Usage python3.7 merge_ydata.py file1.txt file2.txt ... [extra.txt]
# T O D O Statistics file created.


import sys
from random import *
from re import *


def process(input_data):
    results = set([])
    white_space = compile(r"\s")
    for inp in input_data:
        inp = white_space.sub("", inp)
        if inp != '':
            results.add(inp)
    return sorted(results)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = []
        first = 0
        pattern = compile(r"merge_ydata")
        for file_location in sys.argv:
            file_location = file_location.strip()
            if pattern.match(file_location):
                first += 1
            elif first > 0:
                with open(file_location, 'r') as input_data_file:
                    the_input_data = input_data_file.read()
                    data.extend(process(the_input_data.split(",")))
        the_results = sorted(set(data))
        id = round(random() * 10000)
        f = open(str(id) + ".out.txt", "w")
        f.write(",".join(the_results))
        exit(0)
    else:
        print('This test requires some input files.')
        exit(1)
