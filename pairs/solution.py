#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    arr_dic = {}
    for iter2,ele2 in enumerate(arr):
         arr_dic[ele2] = 1
         #arr_dic[]

    for iter1,ele1 in enumerate(arr):
        if(ele1+k in arr_dic.keys()):
            count+=1
            print(ele1,ele1+k)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

