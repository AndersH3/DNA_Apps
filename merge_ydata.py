#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Use only with files in ftdna format
# you can reformat your data with [https://ytree.morleydna.com/extractFromAutosomal]
# just copy and paste the data from the last step into a file.
# But do not hand edit the data.
# If you want to manually add some snps add them into a separate file eg extra.txt.
# Usage python3.7 merge_ydata.py file1.txt file2.txt ... extra.txt



import sys
from random import *
from re import *


def process(input_data):
    results = set([])
    positive = set([])
    negative = set([])
    white_space = compile(r"\s")
    for inp in input_data:
        inp = white_space.sub("", inp)
        if inp != '':
            results.add(inp)
            if inp.endswith('+'):
                positive.add(inp)
            elif inp.endswith('-'):
                negative.add(inp)
            else:
                print(inp)
    return [sorted(results), sorted(positive), sorted(negative)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = []
        data_positive = []
        data_negative = []
        first = 0
        pattern = compile(r"merge_ydata")
        for file_location in sys.argv:
            file_location = file_location.strip()
            if pattern.match(file_location):
                first += 1
            elif first > 0:
                with open(file_location, 'r') as input_data_file:
                    the_input_data = input_data_file.read()
                    res = process(the_input_data.split(","))
                    data.extend(res[0])
                    data_positive.extend(res[1])
                    data_negative.extend(res[2])
        nr = round(random() * 10000)
        f = open(str(nr) + ".out.txt", "w")
        f.write(",".join(sorted(set(data))))
        f = open(str(nr) + ".positive.out.txt", "w")
        f.write(",".join(data_positive))
        f = open(str(nr) + ".negative.out.txt", "w")
        f.write(",".join(data_negative))
        report = "snps: " + str(len(data)) + "   " \
                 + "snps(positive): " + str(len(data_positive)) + "   " \
                 + "snps(negative): " + str(len(data_negative)) + "   "
        f = open(str(nr) + ".report.out.txt", "w")
        f.write(report)
        exit(0)
    else:
        print('This requires some input files.')
        exit(1)
