# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:27:11 2019

@author: Ronan Murphy 15397831
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
input = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
out = [[1, 1, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 0]]

"""
solve method used to to convert input into output
reverse the input using the [::-1] function 
then add the reversed input to the original ouput
return this array
"""
def solve(inputs):
    p = inputs[::-1]
    inputs+=p
    out = inputs
    return out

output = solve(input)
print(output)
