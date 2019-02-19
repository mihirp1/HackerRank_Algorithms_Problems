#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
        limit = n//m + 1
        list1 = range(1,n+1)
        large_list = []
        count = 0
        for i in range(1,limit+1):
            large_list.extend(list1)
            
        del large_list[:s-1]
        
        for element in large_list:
            count += 1
            if(count == m):
                return element 
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

