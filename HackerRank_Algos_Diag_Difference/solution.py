#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    element = ''
    #print(a)
    sum1 = 0
    sum2 = 0
    
    for index,element in enumerate(a):
        sum1 = sum1 + element[index]
        #print(element[index])
        sum2 = sum2 + element[(n-index-1)]
        #print(element[(n-index-1)])
    return(abs(sum1-sum2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()

