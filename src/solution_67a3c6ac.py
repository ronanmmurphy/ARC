# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:21:33 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
import numpy as np
import sys
import format_json as fj

file = str(sys.argv[1])
train_in,train_out,test_in,test_out = fj.read_file(file)
"""
input = [[7, 6, 1], [6, 7, 6], [6, 2, 2]]
out = [[1, 6, 7], [6, 7, 6], [2, 2, 6]]


solve method used to to convert input into output
fliplr numpy function used to reverse each argument
This is then outputted
"""


def solve(inputs):
    outter =[]
    for i in range(len(inputs)):
        inp_array = np.array(inputs[i])
        out=np.fliplr(inp_array).tolist()
        outter.append(out)
    return outter

fj.print_out(train_in, train_out, test_in, test_out, solve)
