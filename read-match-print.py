#!/usr/bin/python3

import re
import sys

# regular expresion that looks for any line that has a space at the beggining

json = re.compile('^\s.')

with open(sys.argv[1], 'r') as my_file:

    for line in my_file:
        if re.search(json, line):
            print(line)

