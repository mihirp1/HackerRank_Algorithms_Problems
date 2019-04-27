#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count_d = {}
    empty_list = []

    count_d = Counter(arr)
    mc = count_d.most_common(1)
    count = count_d.most_common(1)[0][1]
    print("Most Common : ",count)
    print(mc[0][0])

    for key1,ele1 in count_d.items():
        if(ele1 == count):
            empty_list.append(key1)

    return(min(empty_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

