#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    down = 0
    up = 0
    valley_count = 0
    count = 0

    for iter1,letter in enumerate(s):
        if(letter == 'U'):
            up += 1
            count += 1

        if(letter == 'D'):
            down += 1
            count -= 1 

        if(count == 0 and s[iter1] != 'D'):
            valley_count += 1


        print(valley_count,count,letter,up,down)

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

