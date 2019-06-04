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


    while(iter1 < len(arr)):
        print("Outer Loop")
        while(iter2 < len(arr)):
            
            if(iter1 != iter2):
                if(abs(arr[iter1]-arr[iter2]) < min1):
                    print("Inner Loop")
                    min1 = abs(arr[iter1]-arr[iter2])
                    print(min1,arr[iter1],arr[iter2])
            iter2+=1
        iter2 =iter1+1

            #iter2+=1
        iter1+=1


    return min1  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

