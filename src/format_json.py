# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:30:39 2019

@author: Ronan
"""
import json

"""
read_file is used to open the json file load is and split the data input
into training and test for the input and output data
this is done so the print_out method can compare correctly the data and the 
output of the solve method for each function.
"""
def read_file(file):
    """
    open the file and load it using the json import
    """
    input_file = open(file)
    data = json.load(input_file)
    """
    split the data into each category based on the json names 'test' and train sets
    split between the labels of each section iterated through and saved as the input
    data which is returned in four seperate parts
    """
    train_input = [data['train'][i]['input'] for i in range(len(data['train']))]
    train_output = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_input = [data['test'][i]['input'] for i in range(len(data['test']))]
    test_output = [data['test'][i]['output'] for i in range(len(data['test']))]
    return train_input,train_output,test_input,test_output

"""
Function print_out is called by each python script to test the if the output result is the same
as desired
"""
def print_out(train_input, train_output, test_input, test_output, solve):
    output = solve(train_input)
    print("Train\n", train_input)
    print("Output\n", output)
    if(train_output == output):
        print("Training Correct")
        
    
    output = solve(test_input)
    print("Test\n", test_input)
    print("Output\n", output)
    if(test_output== output):
        print("Test Correct")
        
