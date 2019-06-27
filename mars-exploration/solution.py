#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    s1 = range(0,99,3)
    s2 = range(1,99,3)
    s3 = range(2,99,3)
    count = 0
    for iter1,ele1 in enumerate(s):
        if(iter1 in s1 and s[iter1] != 'S'):
          count+=1
        if(iter1 in s2 and s[iter1] != 'O'):
          count+=1
        if(iter1 in s3 and s[iter1] != 'S'):      
          count+=1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

