#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    iter1=0
    iter2=0
    element=0
    sum1=0
    count=0
    counter=0
    if(n!=1):
     for iter1,element in enumerate(s):
         iter2 = iter1 + m
         sum1 = 0
     
         while(iter1 < iter2 and iter2 < n and iter1 != iter2):
             #print(iter1)
             sum1 = sum1 + s[iter1]
             #print(sum1)
             if(sum1 == d):
              count = count+1
             iter1 = iter1 + 1
            
     #print(count)
         
    elif(n==1):
        if(s[0] == (d*m) ):
            count = 1
        else:
            count = 0
        
    return count
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

