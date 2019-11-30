# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:27:11 2019

@author: Ronan
Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
"""
input = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
output = [[1, 1, 0], [1, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 0]]

p = input[::-1]

input+=p
print(input)
