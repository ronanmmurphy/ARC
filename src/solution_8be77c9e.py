# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:27:11 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""

import sys
import format_json as fj
"""
input = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
out = [[1, 1, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 0]]
"""


file = str(sys.argv[1])
train_in,train_out,test_in,test_out = fj.read_file(file)

"""
solve method used to to convert input into output
reverse the input using the [::-1] function 
then add the reversed input to the original ouput
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

fj.print_out(train_in, train_out, test_in, test_out, solve)

