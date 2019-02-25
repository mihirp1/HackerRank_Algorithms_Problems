#!/bin/python3

#THIS SOLUTION IS NOT OPTIMUM and has been optimized in solution1

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import permutations
from itertools import combinations 
from collections import defaultdict
from collections import Counter   


def fact(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n



# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    unique_s = list(set(s))
    repeat_char_dic = {}
    repeat_char_dic = Counter(s)
       
    List_Of_StringWindows = []

    window_size_list = range(2,len(s)-1)
    element = ''

    #it = 0
    size_dict = defaultdict(list)
    

    while( len(s) > 1 ):
     for it in range(1,len(s)+1):
        SLICE = slice(it)
        

        element = s[SLICE] 
        l_ele = len(element) 
        if(len(element) > 1 ):
          #print(element)
          size_dict[l_ele].append(element)  
         #List_Of_StringWindows.append(element)
     s = (s[1:])
     #print("*")
     #print(s)
     #print("*")
    
    #print(size_dict)
    final_count = 0

    #combos = combinitions(unique_s)
    #perms = permutations()
    string = ''
    string1 = ''


    for key,value in size_dict.items():
        #print("key.value")
        #print(key,value)
        for iter1,string in enumerate(value):  
         for iter2,string1 in enumerate(value):
             if(iter1 != iter2):
                 if(Counter(string1) == Counter(string)):
                     print(string,string1)
                     final_count += 1


    repeated_count = 0
    

    print(repeat_char_dic)
    for key,value in repeat_char_dic.items():
        if(int(value) > 1):
            print("key,fact")
            
            fac = fact(value - 1)
            print(key,fac)
            repeated_count += fac 


    return final_count//2 + repeated_count  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

