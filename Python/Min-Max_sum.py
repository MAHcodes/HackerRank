#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxsum = 0
    sumnum = 0
    sums = []
    for i in range(len(arr)):
        sumnum += sum(arr[i+1:])
        sumnum += sum(arr[:i])
        sums.append(sumnum)
        sumnum = 0
    minsum = sums[0]
    for x in sums:
        if x > maxsum:
            maxsum = x
        elif x < minsum:
            minsum = x
    print(minsum, maxsum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
