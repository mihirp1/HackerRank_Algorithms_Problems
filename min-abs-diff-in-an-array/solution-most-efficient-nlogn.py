#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min1 = 1000000000
    iter1 = 0
    iter2 = 0
    arr.sort() 

    for iter1,ele1 in enumerate(arr):
        if(iter1 < len(arr) -1):
            if(abs(arr[iter1] - arr[iter1+1]) < min1):
                min1 = abs(arr[iter1] - arr[iter1+1])


    return min1  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

