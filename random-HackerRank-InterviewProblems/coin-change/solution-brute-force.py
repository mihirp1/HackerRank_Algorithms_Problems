#!/bin/python3

import math
import os
import random
import re
import sys 
from itertools import combinations

# Complete the getWays function below.
def getWays(n, c):
    e = 0
    master_list = []
    count = 0
    
    for num in c:
        limit = n//num
        e = num
        l1 = [e for number in range(limit)]
        master_list += l1
        
    #print(master_list)
    
    for i in range(1,n+1):
        for unit in ((list(set((list(combinations(master_list,i))))))):
            if(sum(unit) == n):
                count +=1
                
    return(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    fptr.write(str(ways))

    fptr.close()

