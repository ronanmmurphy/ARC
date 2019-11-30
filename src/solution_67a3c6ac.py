# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:21:33 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
import numpy as np
input = [[7, 6, 1], [6, 7, 6], [6, 2, 2]]
out = [[1, 6, 7], [6, 7, 6], [2, 2, 6]]

"""
solve method used to to convert input into output
fliplr numpy function used to reverse each argument
This is then outputted
"""
def solve(inputs):
    
    out=np.fliplr(inputs)
    
    return out


output = solve(input)
print(output)