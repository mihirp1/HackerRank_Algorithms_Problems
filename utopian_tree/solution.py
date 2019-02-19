#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
        #print("Here : ")
        #print(1%2)
        #i = 0
        height = 1

        for i in range(0,n):
         if(i == 0):
            pass
         
         #if(i == 1):
            #height += 1
            
         if(i%2 == 0):
            height = height *2                     
        
         if(i%2 != 0):
            height += 1
            print("I am 1")

        #return (height)
        return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

