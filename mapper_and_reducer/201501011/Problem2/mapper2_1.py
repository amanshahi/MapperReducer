#!/usr/bin/python

import sys

count = 0
for line in sys.stdin:
    if count == 0:
        count += 1
        pass
    else :
        data = line.strip().split(",")
        if len(data) == 7:
            print data[5]

