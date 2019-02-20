#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter = 0

    print(s[:4])

    for letter in s:
        if(letter == "a"):
          counter += 1

    preliminary_count = 0

    string_length = len(s)

    seq_n = n // string_length

    preliminary_count = counter * seq_n

    diff = n % string_length

    skeletal_string = s[:diff]

    if(diff != 0):
      for elem in skeletal_string:
        if(elem == "a"):
           preliminary_count += 1
            
    print(skeletal_string)
    return preliminary_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

