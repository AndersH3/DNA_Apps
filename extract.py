#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Usage:
# python3.7 ./extract.py yseq_data.txt
#

from random import *
from re import *
from sys import *

# SampleID	Ordered	Marker+	Chr	Start	End	Allele
if __name__ == '__main__':
    pattern = compile(r"\d+[\t]\S+[\t](?P<Marker>\S+)[\t]\w+[\t]\d+[\t]\d+[\t]\S+(?P<SGN>[-+])\n")
    file = argv[1]
    nr = round(random() * 10000)
    name = str(nr) + "-" + file
    outfile = open(name, 'w')
    first = ""
    with open(file, 'r') as input_data_file:
        lines = input_data_file.readlines()
        for line in lines:
            matches = pattern.search(line)
            if matches != None:
                marker = matches.group("Marker")
                sgn = matches.group("SGN")
                if marker != None and marker != None:
                    outfile.write(first + marker + sgn)
                    if first == "":
                        first = ","
    outfile.close()
