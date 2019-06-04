#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min1 = 1000000000


    for iter1,ele1 in enumerate(arr):
        for iter2,ele2 in enumerate(arr):
            if(iter1 != iter2):
                if(abs(ele1-ele2) < min1):
                    min1 = abs(ele1-ele2)
                    if(min1 == 3):
                        return 3
                #elif(abs(ele2-ele1) < min1):
                    #min1 = abs(ele2-ele1)

    return min1  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

