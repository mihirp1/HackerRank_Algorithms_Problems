#!/bin/python3

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


def CheckCount(cc):
    flag = 1
    for k1, element in cc.items():
        if(cc[k1] > 1):
         flag = 0   
         return False
    
    if(flag == 1):
        return True
    
   

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    #unique_s = list(set(s))
    #repeat_char_dic = {}
    #repeat_char_dic = Counter(s)
       
    #List_Of_StringWindows = []

    #window_size_list = range(2,len(s)-1)
    
    element = ''

    #it = 0
    list_size = len(s)
    size_dict = defaultdict(list)

    u_c = Counter(s)
    

    while( len(s) > 0 ):
     for it in range(1,len(s)+1):
        SLICE = slice(it)
        
        element = s[SLICE] 
        l_ele = len(element) 
        if(len(element) > 0 and len(element) != (list_size)):
          #print(element)
          c_counter = Counter(element)
          if(Counter(element)):
            size_dict[l_ele].append(element)  
         #List_Of_StringWindows.append(element)
     s = (s[1:])
     #print("*")
     #print(s)
     #print("*")
    
    print(size_dict)
    final_count = 0

    #combos = combinitions(unique_s)
    #perms = permutations()
    string = ''
    string1 = ''


    counter_list = []
    repeated_count = 0
    #print(size_dict)
    '''
    for key,value in size_dict.items():                
        for iter1,string in enumerate(value):  
         for iter2,string1 in enumerate(value):
             if(iter1 != iter2 and Counter(string1) == Counter(string)):   
                     #print(string,string1)
                     final_count += 1
    '''

    [counter_list.append(1) for key,value in size_dict.items() for iter1,string in enumerate(value) for iter2,string1 in enumerate(value) if(iter1 != iter2 and Counter(string1) == Counter(string)) ]

    print(size_dict)
    final_count = sum(counter_list)//2

    return final_count  

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

