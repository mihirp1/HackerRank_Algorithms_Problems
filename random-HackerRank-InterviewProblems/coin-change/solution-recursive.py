#!/bin/python3

import math
import os
import random
import re
import sys 
from itertools import combinations

# Complete the getWays function below.
def getWays(n, c,m):
    
    if(n == 0):
        return 1
    
    if(n < 0):
        return 0
    
    if (m <=0 and n >= 1): 
        return 0
        
    

                
    return getWays(n,c,m-1) + getWays(n-c[m-1],c,m)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c,m)
    fptr.write(str(ways))

    fptr.close()

