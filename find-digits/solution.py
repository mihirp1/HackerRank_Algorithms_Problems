#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    n = str(n)
    new = []
    num_list = []
    num1 = 0
    if(len((n)) == 1):
        count += 0
        print("Here")

    if(len(n) > 1):    

     for ele in n:
         if(int(ele) != 0):
             num1 = int(n)%int(ele)
             if ( num1 == 0):
               count+=1
              

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

