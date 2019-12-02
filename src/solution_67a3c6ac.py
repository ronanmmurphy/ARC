# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:21:33 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
import numpy as np
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
iterat through outter array
fliplr numpy function used to reverse each argument
this is appended to the outter array to retaint the format
This is then outputted
"""
def solve(inputs):
    outter =[]
    for i in range(len(inputs)):
        inp_array = np.array(inputs[i])
        out=np.fliplr(inp_array).tolist()
        outter.append(out)
    return outter
"""
Compares the input and output data calling the print_out function
"""

fj.print_out(train_input,train_output,test_input,test_output, solve)
