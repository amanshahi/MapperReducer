#!/usr/bin/python
import sys
import os
cnt_of_data = 0
old_data = -1

for read in sys.stdin:
    var = read.strip()

    if old_data != -1 and old_data != var:
        print old_data, ",", cnt_of_data
        cnt_of_data = 0

    old_data = var
    cnt_of_data += 1

#last data value
if old_data != -1:
    print old_data, ",", cnt_of_data