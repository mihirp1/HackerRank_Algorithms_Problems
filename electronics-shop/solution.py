#!/bin/python3

import os
import sys
from itertools import combinations

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #kbs = list(combinations(keyboards,1))
    #drvs = list(combinations(drives,1))
    #print(kbs)
    #print(drvs)
    kbs = len(keyboards)
    drv = len(drives)
    sum_list = []
    count = 0
    FLAG = 0
    i = 0
    j= 0
    
    for i in keyboards:
        #count += 1
        for j in drives:
            #count += 1
            if ((i+j) < b or (i+j) == b):
                FLAG = 1
                sum_list.append(i+j)
                #if(count == (kbs*drv)):
    if(FLAG == 1):
     return max(sum_list)
    if(FLAG == 0):            
     return (-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    
    
    

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

