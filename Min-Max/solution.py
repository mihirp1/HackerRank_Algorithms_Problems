#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    combo = combinations(arr,4)
    combo = list(combo)
    my_list = []
    for ind in combo:
        my_sum = sum(list(ind))
        my_list.append(my_sum)
    print (min(my_list),max(my_list))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

