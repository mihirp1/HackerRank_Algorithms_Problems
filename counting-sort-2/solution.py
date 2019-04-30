#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    max_n = max(arr)
    buckets = [0] * (max_n + 1)
    sl = []

    print(buckets)

    for iter1,ele1 in enumerate(arr):
        #print(buckets[ele1])
        buckets[ele1] += 1

    for iter2,ele2 in enumerate(buckets):
        for iter3 in range(ele2):
            sl.append(iter2)

    return sl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

