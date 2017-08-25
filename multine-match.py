#!/usr/bin/python3

import re
import sys

json1 = re.compile(r"^{", re.MULTILINE)
# json2 = re.compile(r"(^[^>][\w\s]+)$", re.MULTILINE|re.DOTALL)

# regular expresion that looks for any line that has a space at the beggining


with open(sys.argv[1], 'r') as my_file:
    for line in my_file:

        if re.search(json1, line):
            print(line)
