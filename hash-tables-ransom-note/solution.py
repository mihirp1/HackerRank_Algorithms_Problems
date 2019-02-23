#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    dictionary = (Counter(note) - Counter(magazine))
    '''
    print("mag")
    print(Counter(magazine))
    print("note")
    print(Counter(note))
    
    
    print("mag-note")
    print(Counter(magazine) - Counter(note))
    
    print("note-mag")
    print(Counter(note) - Counter(magazine))
    '''

    if(not bool(dictionary)):
        print("Yes")

    else:
        print("No")


    '''
 mag_dic = {}
 note_dic = {}
 flag = "yes"
 flag1 = "twice"
 for magword in magazine:
     count = 0
     for magword1 in magazine:
         if(magword == magword1):     
            count += 1 
            mag_dic[magword] = count
 count = 0
 for noteword in note:
     count = 0
     for noteword1 in note:
         if(noteword == noteword1):
            count += 1
            note_dic[noteword] = count

 for key,di_ele in note_dic.items():
     try :
       if(note_dic[key] > mag_dic[key]):           
          print("No")
          flag = "no"
          break
     except:
         print("No")
         flag1 = "once"   
         KeyError

 if(flag != "no" and flag1 != "once"):
         print("Yes")
'''



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

