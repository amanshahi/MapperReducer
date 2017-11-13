#!/usr/bin/python
import sys
import os

cnt_of_data = 0
old_data, max_data = -1, -1
max_country = ''

for read in sys.stdin:
    var = read.strip()

    if old_data != -1 and old_data != var:
        if cnt_of_data > max_data:
            max_data = cnt_of_data
            max_country = old_data
        cnt_of_data = 0

    old_data = var
    cnt_of_data += 1

#last data value
if old_data != -1 and cnt_of_data > max_data:
    max_data = cnt_of_data
    max_country = old_data
print max_country, max_data
