#This approach 1 fails 4 out of 14 test cases. solution 2 is more optimal


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr):
    Sorted_flag = 1
    source_iter = 0
    count = 0
    main_count = 1
    l = 0     
    l = len(arr)

    for iter1,ele in enumerate(arr):
        if(iter1 < len(arr) - 1):
         if( arr[iter1 + 1] - arr[iter1] != 1):
           Sorted_flag = 0
           #print("CHECK")
           break


    if(Sorted_flag == 1):
        return 0


    for iter4,el4 in enumerate(arr):
        if(iter4 < len(arr) - 1):
         if( arr[iter4] != iter4+1):
           main_count += 1 
           #print("CHECK")

    if(Sorted_flag == 0):
     for iter2,ele2 in enumerate(arr):
        if(iter2 < len(arr) - 1):
         if(ele2 != iter2 + 1):           
            source_iter = arr.index(iter2 + 1)
            #source_iter = arr.index(2)
            print(source_iter,iter2+1)
            print(arr)
            arr[iter2] = arr[source_iter]
            arr[source_iter] = ele2
            count += 1
      

            #print("Calculating...")

     return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

