#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.

def finditer(arr,ele):
    ans = 0
    try:
       ans = (arr.index(ele)) 
       return ans 
    except: ValueError

def beautifulTriplets(d, arr):
    count = 0    
    for iter1,ele1 in enumerate(arr):
        if(iter1 < len(arr) - 2):
            index1 = finditer(arr,arr[iter1]+d)
            index2 = finditer(arr,arr[iter1]+2*d)

            if(index1 is not None and index2 is not None):
             if(iter1 < index1 and index1 < index2):
              #if((arr[iter1+1] - arr[iter1]) == (arr[iter1 + 2] - arr[iter1 + 1])):
              count +=1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

