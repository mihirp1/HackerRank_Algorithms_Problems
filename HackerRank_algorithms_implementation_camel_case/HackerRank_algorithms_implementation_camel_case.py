#!/bin/python3

import sys

def camelcase(s):
    # Complete this function
    #string_list = []
    iter1=1
    iter2=0
    element1=''
    element2=''
    string_list = list(s)
    length = len(string_list)
    first = 0
    second = 0
    new_list = {}
    count = 0
    #print(string_list)
     
    for iter1,element1 in enumerate(string_list):
         #print(string_list[iter1])
         if((string_list[iter1 -  1]).islower() and (string_list[iter1]).isupper() and (string_list[iter1 +1]).islower()):
            count += 1
                
    return (count+1)

if __name__ == "__main__":
    s = input().strip()
    #print(type(s))
    result = camelcase(s)
    print(result)

