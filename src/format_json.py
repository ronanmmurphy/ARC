# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:30:39 2019

@author: Ronan
"""
import matplotlib.pyplot as plt
import json

def read_file(file):
    input_file = open(file)
    data = json.load(input_file)
    
    train_in = [data['train'][i]['input'] for i in range(len(data['train']))]
    train_out = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_in = [data['test'][i]['input'] for i in range(len(data['test']))]
    test_out = [data['test'][i]['output'] for i in range(len(data['test']))]
    return train_in,train_out,test_in,test_out

def print_out(train_in, train_out, test_in, test_out, solve):
    ##training
    print("\n\nTraining")
    output = solve(train_in)
    print("Output:\n", output)
    if(train_out == output):
        print("Training Data Verified!!!")
    ##training
    print("\n\nTesting")
    output = solve(test_in)
    print("Output:\n", output)
    if(test_out== output):
        print("Testing Data Verified!!!\n")
        
def graphic(input):
    
    """
    Function to plot grids and emulate testing interface.
    input = A list of test input and computed output. 
    """
    for i in range(len(input)):
        plt.matshow(input[i])
        plt.show()
    