# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:42:17 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
import sys
import format_json as fj
import numpy as np
"""
#import numpy as np
#input = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 8, 8, 8, 8, 8, 0, 8, 8, 8], [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8], [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 8, 0, 8, 8, 8, 8, 8, 8, 8, 8], [0, 1, 1, 0, 1, 1, 1, 1, 0, 8, 0, 8, 8, 0, 8, 8, 8, 0, 8, 8], [1, 0, 1, 1, 1, 1, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 8], [1, 1, 0, 1, 1, 1, 1, 1, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 8, 8, 0, 8, 8, 8, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 6, 6, 6, 6, 0, 6, 6, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0], [6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0], [0, 6, 0, 6, 6, 6, 0, 6, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [6, 6, 6, 0, 6, 6, 6, 6, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [6, 0, 6, 6, 0, 6, 0, 6, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [6, 6, 6, 6, 6, 0, 6, 6, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [6, 6, 6, 6, 6, 0, 6, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [6, 6, 6, 0, 6, 6, 0, 6, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0], [6, 0, 0, 0, 6, 0, 6, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [6, 6, 0, 6, 0, 6, 6, 6, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]]
ou = [[1,8], [6,1]]
input = [[4, 4, 4, 4, 4, 0, 0, 8, 0, 8, 8, 8, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3], [4, 4, 4, 0, 0, 4, 0, 8, 8, 8, 8, 8, 0, 0, 3, 3, 3, 3, 0, 3, 3, 0], [4, 4, 4, 4, 0, 0, 0, 8, 8, 0, 0, 8, 0, 0, 3, 3, 3, 0, 3, 0, 3, 3], [4, 4, 0, 0, 4, 4, 0, 8, 8, 8, 8, 8, 8, 0, 3, 3, 3, 3, 0, 3, 3, 3], [4, 4, 4, 4, 4, 4, 0, 0, 8, 8, 8, 8, 8, 0, 3, 0, 3, 0, 3, 0, 3, 0], [0, 0, 4, 4, 4, 4, 0, 8, 0, 8, 0, 8, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3], [4, 4, 0, 4, 4, 0, 0, 8, 8, 8, 8, 0, 8, 0, 3, 0, 0, 3, 3, 3, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 2, 0, 2, 2, 2, 2, 0, 8, 0, 8, 0, 0, 8, 8, 8], [1, 0, 1, 1, 0, 1, 0, 2, 0, 2, 2, 2, 0, 0, 8, 8, 8, 0, 0, 8, 8, 8], [1, 1, 1, 0, 1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8], [1, 1, 0, 1, 0, 1, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 8, 8, 8, 0, 8, 8], [1, 1, 1, 0, 1, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 8, 0, 8, 8, 8, 8, 0], [1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 0, 2, 0, 8, 8, 0, 0, 8, 0, 8, 8], [1, 1, 1, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 8, 8, 0, 0, 0, 8, 8, 8], [1, 0, 0, 1, 0, 1, 0, 2, 2, 0, 2, 2, 0, 0, 8, 0, 8, 8, 0, 0, 0, 8], [1, 1, 1, 1, 0, 1, 0, 0, 2, 2, 2, 0, 2, 0, 0, 8, 8, 0, 0, 0, 8, 0], [1, 1, 0, 1, 1, 1, 0, 2, 2, 2, 0, 2, 0, 0, 8, 0, 8, 8, 0, 0, 8, 8]]
o = [[4, 8, 3], [1, 2, 8]]
"""
"""
solve method used to to convert input into output
first the input data is filtered to remove any zeros from the input
this is done using the numpy method filter()
then for each filtered input array a list is created to add unique numbers in each 
pattern, if they are unique they are added to my list
if the list is greater than zero a final filter is used to return only unique patterns
this will reduce the the output to a one or more sets of unique number patterned arrays
this list is returned and printed

"""
file = str(sys.argv[1])
train_in,train_out,test_in,test_out = fj.read_file(file)

def solve(inputs):
    
    out = []
    for i in inputs:
        fil = filter(None, i)
        mylist = list()
        for j in fil:
            if j not in mylist:
                mylist.append(j)
                
        if len(mylist)>0 and mylist not in out:
            out.append(mylist)
        
    return out
        


for inputs in (train_in + test_in):
    outputs = solve(inputs)
    print(outputs)
    print()



