#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    element1 = 0
    element2=0
    iter1=0
    iter2=0
    count = 0
    numbers = {}
    ans =0
    key1 = 0
    value1=0
    count1=0
    final_list = []
    
    highest_given = 0
    new_list = []
    for iter1,element1 in enumerate(ar):
        count = 0
        for iter2,element2 in enumerate(ar):
         if(ar[iter1] == ar[iter2]):
                count += 1
                new_list.append(count)
        ans = ar[iter1]
        numbers[ans] = count
        #highest_given = max(new_list)
        
 
    highest_given = max(new_list)
 
  

        
    for key1,value1 in numbers.items():
       if (numbers[key1] == highest_given):
        final_list.append(key1)
                  
            
        
    return( min(final_list))    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

