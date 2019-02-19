#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    iter1 = 0
    flag = 0

    if(len(c) == 2 and c[len(c) -1] == 0 and c[len(c) - 2] == 0):
     return 1
    
    while(iter1 < len(c) - 2  ) :
         if(c[iter1 + 2] == 0):
           iter1 += 2
           count += 1
           flag  = 1

         if(flag == 0 and c[iter1+1] == 0):
           iter1 += 1
           count += 1
         print(count,iter1,flag)
         flag = 0

    if(c[len(c) - 1] == 0 and c[len(c) - 2] == 0 and c[len(c)- 3] != 0):
           count += 1

    print(count)     
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

