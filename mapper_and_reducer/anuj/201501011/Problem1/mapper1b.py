#!/usr/bin/python
import sys
import os
index, answer = 0, ''

for read in sys.stdin:
    if index == 0:
        index = 1
        continue
    else:
        var = read.split(",")
        if len(var) == 7:
            answer += str(var[5])
            answer +='\n'
print answer

