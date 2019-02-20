#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np

# Complete the hourglassSum function below.
def hourglassSum(arr):
   sum1 = 0
   array_of_sum = []
   for i in range(4):
       for j in range(4):
           sum1 += arr[0+i][0+j] + arr[0+i][1+j] + arr[0+i][2+j] + arr[1+i][1+j] +               arr[2+i][0+j] + arr[2+i][1+j] + arr[2+ i] [2+j]
           array_of_sum.append(sum1)
           sum1 = 0
   print(array_of_sum)
   return(max(array_of_sum))
   # j is in range 4
   # i is in range 4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

