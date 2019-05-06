#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    string_list = []
    iter1=0
    iter2=0
    element1=''
    element2=''
    string_list = list(password)
    length = len(string_list)
    first = 0
    second = 0
    new_list = []
    count = 0
    islower = 0
    isdigit = 0
    isspecial = 0
    isupper = 0
    islength6 = 0
    LENGTH = 0
    higher_length = 0
    length_needed = 0
    missing_categ = 0
    #print(length)
    if(length == 6 or length > 6):
        LENGTH = 1
    if(LENGTH == 1): 
     #print("FIRST THINGS FIRST")
     for iter1,element1 in enumerate(password):
         if((password[iter1]).islower()):
            islower = 1
            count += 1
         if((password[iter1]).isupper()):
            isupper = 1
            count += 1
         if((password[iter1]).isdigit()):
            isdigit = 1
            count += 1
         if(len(password) == 6):
            islength6 = 1
            count += 1
         if(not (password[iter1]).isalpha() and not (password[iter1]).isdigit()):
            isspecial = 1
            count += 1
     higher_length = islower + isupper + isdigit + isspecial
    
        
     return (4 - higher_length)
    
    if(LENGTH != 1):
        #print("SECOND THINGS SECOND")
        for iter1,element1 in enumerate(password):
         if((password[iter1]).islower()):
            islower = 1
            count += 1
         if((password[iter1]).isupper()):
            isupper = 1
            count += 1
         if((password[iter1]).isdigit()):
            isdigit = 1
            count += 1
         if(not (password[iter1]).isalpha() and not (password[iter1]).isdigit()):
            isspecial = 1
            count += 1
        higher_length = islower + isupper + isdigit + isspecial
        missing_categ = 4 - higher_length
        length_needed = 6 - length
        #print(length_needed)
        #print(length)
        if(length_needed == missing_categ or length_needed < missing_categ):
            return(missing_categ)
        if(length_needed > missing_categ):
            return(length_needed)
    #return (4 - higher_length)
if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

