#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    #index_number = []
    complete_list = []
    final_list = []
    min_list = []
    diff = 0

    def onesort(ele):
        return ele[1]

    for iter1,ele1 in enumerate(price):
         complete_list.append([iter1,ele1])
    
    complete_list.sort(key=onesort,reverse=True)

    print(complete_list)


    for iter2,ele2 in enumerate(complete_list):
        if(iter2 < len(complete_list) - 1):
          if(complete_list[iter2][0] < complete_list[iter2+1][0]):
             diff = complete_list[iter2][1] - complete_list[iter2+1][1]
             min_list.append(diff)

    return(min(min_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

