#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    dict_1 = {}
    dict_2 = {}
    diff = {}
    dict_1 = Counter(arr)
    dict_2 = Counter(brr)
    diff = dict_2 - dict_1

    return(sorted(list(diff.keys())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

