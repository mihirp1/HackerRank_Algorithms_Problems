#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    iter1 = 0
    iter2 = 0
    iter3 = 0
    value1 = 0
    value2 = 0
    value3 = 0
    colour_map = {}
    count = 0
    new_list = []
    ans = 0
    sum1 = 0
    even_sum = 0
    
    
    for iter1,element1 in enumerate(ar):
        count = 0
        for iter2,element2 in enumerate(ar):
         if(ar[iter1] == ar[iter2]):
                count += 1
                new_list.append(count)
        ans = ar[iter1]
        colour_map[ans] = count
        #highest_given = max(new_list)
        
    for iter3,value3 in colour_map.items():
        sum1=0
        if(colour_map[iter3] != 1):
            sum1 = colour_map[iter3]//2
            #print(sum1)
            even_sum = even_sum + sum1 
        
    #print(colour_map)
    return even_sum
 
         

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

