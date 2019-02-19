#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_oranges = 0
    total_apples = 0
    for apple in apples:
     d = apple
     if (d > 0):
        if ((a+d) > s or (a+d == s)) and ((a+d) < t or a+d == t):
            total_apples = total_apples +      1
      
    for orange in oranges :
     d = orange   
     if d < 0 :
        d = d * -1
        if ((b-d) > s or (b-d) == s) and ((b-d) < t or b-d == t): 
            total_oranges = total_oranges +  1
        
    print(total_apples)
    print(total_oranges)
        

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

