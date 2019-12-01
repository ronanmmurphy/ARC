# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:42:17 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
import sys
import format_json as fj
"""
import sys and format json to give ability to read in json files
"""

"""
reads in the json files and splits the data into train and test
"""

file = str(sys.argv[1])
train_input,train_output,test_input,test_output = fj.read_file(file)
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
        
"""
Compares the input and output data calling the solve method for the input data iterated over a loop
to change it to a 2D array
"""

for inp in (train_input + test_input):
    outputs = solve(inp)
    print(outputs)
    print()



