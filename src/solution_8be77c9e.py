# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:27:11 2019

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
reverse the input using the [::-1] function 
then add the reversed input to the original ouput
using the extend function
append the array to another outter array to return the correct format
return this array
"""

def solve(inputs):
    out =[]
    for i in range(len(inputs)):
        inp =  inputs[i]
        inp_array = inputs[i]
        reverse = inp_array[::-1]
        inp.extend(reverse)
        out.append(inp)
        
    return out

"""
Compares the input and output data calling the print_out function
"""

fj.print_out(train_input, train_output, test_input, test_output, solve)

