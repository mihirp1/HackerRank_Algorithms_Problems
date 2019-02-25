#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter    


s1 = "abcdefghiijjkkwhga"
s2 = "nnggfffhhrtwsoqpla"
s3 = "abab"
s4 = "baba"

s31 = Counter(s3)
s41 = Counter(s4)

if(s31 == s41):
  print("YES")
