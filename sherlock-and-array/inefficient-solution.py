#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    sum1 = sum(arr)
    iter1 = 0
    flag = 0
    if(len(arr) == 1):
        flag = 1
        return("YES")

    if(len(arr) > 1):
        while(iter1 < len(arr) ):
            #pre = arr[:iter1]
            #post = arr[iter1+1:]
            #print("Iter1 : ",arr[iter1])
            #print(pre)
            #print (sum(pre))
            #print(post)
            #print(sum(post))
            lhs = sum(arr[:iter1])
            if( lhs == (sum1 - lhs - arr[iter1])):
                flag = 1
                return("YES")
            iter1+=1
    if(flag == 0):
        return("NO")
    if(flag == 1):
        return("YES")    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

