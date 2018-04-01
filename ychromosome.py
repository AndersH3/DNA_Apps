#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# Use only with files in ftdna format
#you can reformat your data with [https://ytree.morleydna.com/extractFromAutosomal]
#just copy and paste the data from the last step into a file.
#But do not hand edit the data.
#If you want to mannualy add some snps add them into a separate file eg extra.txt.
# Usage python3.6 merge_ydata.py file1.txt file2.txt ... [extra.txt]
# TODO Statistics file created.
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
