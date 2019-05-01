#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    char_l = []
    for ele in s:
        if(ele != " "):
          char_l.append(str(ele).lower()) 
  
    if(len(list(set(char_l))) != 26):
      return("not pangram")

    else:
        return("pangram")  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

