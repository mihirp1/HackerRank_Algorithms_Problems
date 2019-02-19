#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    #print(n)
    #ans = 0
    count = 0
    list1 = list(range(1,n+1))
    del list1[:s-1]
    while(count < m ):
        print("In here")
        if(count == 0):
            print("######")
            for num in list1:
                if(count != m):
                   count += 1
                   if(count == m):
                    return num
        if(count!= m):
            print("********")
            for num2 in list(range(1,n+1)):
                count += 1
                if(count == m):
                    #ans = num2
                    return num2
                    break
        else:
            return count    

    #print(count)        
    #return ans
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

