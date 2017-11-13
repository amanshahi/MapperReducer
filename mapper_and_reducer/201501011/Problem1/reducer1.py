#!/usr/bin/python

import sys

totalCount = 0
oldKey = None

for line in sys.stdin:
    data = line.strip()

    if oldKey and oldKey != data:
        print oldKey, ",", totalCount
        oldKey = data;
        totalCount = 0

    oldKey = data
    totalCount += 1

if oldKey != None:
    print oldKey, ",", totalCount

