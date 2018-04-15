#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Usage:
# python3.7 ./merge.py file,file1,file2... > merged_file.txt
#
#


import sys
from re import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        first = 0
        pattern = compile(r"merge_ydata")
        for file_location in sys.argv:
            file_location = file_location.strip()
            if pattern.match(file_location):
                first += 1
            elif first > 0:

                exit(0)
    else:
        print('This requires some input files.')
        exit(1)
    exit(0)
# else:
#     print('This requires some input files.')
# exit(1)
