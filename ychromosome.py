#!/usr/bin/python
# -*- coding: utf-8 -*-

# Specify output folder as argument(folder is created).
# multiple files as input, processed separate.
#
# Alternative input and output folder(subfolder).
# Working with list of files
# Statistics file created in folder
import sys


def process(input_data):
    results = []
    input_data = input_data.strip().split(",")
    for cell in input_data:
        inp = cell.strip().replace(" ", "").replace("\n", "")
        if inp != '':
            results.append(inp)
    results = sorted(set(results))
    return results


# if __name__ == '__main__':
#    pth = ""
#    file_list = os.listdir("./" + pth)

if len(sys.argv) > 1:
    file_location = sys.argv[1].strip()
    with open(file_location, 'r') as input_data_file:
        the_input_data = input_data_file.read()
else:
    print('This test requires some input files.')
    exit(1)

the_results = process(the_input_data)

new_file_location = file_location + ".out.txt"
f = open(new_file_location, "w")
f.write(",".join(the_results))
exit(0)
