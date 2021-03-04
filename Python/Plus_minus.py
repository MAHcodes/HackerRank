#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zeros = 0, 0, 0
    length = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeros += 1
    print("{:.6f}".format(positive/ length))
    print("{:.6f}".format(negative/ length))
    print("{:.6f}".format(zeros/ length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
