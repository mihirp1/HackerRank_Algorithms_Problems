#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    min1 = 100000000000
    for iter1,ele1 in enumerate(a):
        for iter2,ele2 in enumerate(a):
            if(a[iter1] == a[iter2] and iter1 != iter2):
                if(abs(iter2-iter1) < min1):
                    min1 = abs(iter2-iter1)

    if(min1 == 100000000000):
        return -1

    else:
        return min1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

