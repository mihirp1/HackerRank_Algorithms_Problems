#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


print("H")

d1 = {1:4,2:4,3:3,7:1}


d2 = {1:4,2:4,3:2,7:1}

d1_counter = Counter(d1)
d2_counter = Counter(d2)


print(d1_counter - d2_counter)
