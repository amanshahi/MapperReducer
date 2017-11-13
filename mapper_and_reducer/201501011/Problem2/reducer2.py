#!/usr/bin/python

import sys

totalCount = 0
maxCount = 0
maxCountry = None
oldKey = None

for line in sys.stdin:
    data = line.strip()

    if oldKey and oldKey != data:
        if maxCount < totalCount:
            maxCount = totalCount
            maxCountry = oldKey
        oldKey = data;
        totalCount = 0

    oldKey = data
    totalCount += 1

if oldKey != None and maxCount < totalCount:
    maxCount = totalCount
    maxCountry = oldKey

print maxCountry, ",", maxCount
