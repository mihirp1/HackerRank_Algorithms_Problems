#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    sum1 = 0
    flavours = []
    sorted1 = []

    for iter1,ele1 in enumerate(arr):
        for iter2,ele2 in enumerate(arr):
            #print("Hi")
            if(iter1 != iter2 and arr[iter1] != m and arr[iter2] != m):
                #sum1 = 
                if(arr[iter1] + arr[iter2] == m):
                  print(iter1+1,iter2+1)
                  flavours.append(iter1+1)
                  flavours.append(iter2+1)
                  
                  sorted1 = sorted(flavours)

                  return (sorted1) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

