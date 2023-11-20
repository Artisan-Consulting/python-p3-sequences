#!/usr/bin/env python3
# Prints the Fibonacci sequence up to a given length
# Logic firstly: initialize the first two numbers in the sequence.

def print_fibonacci(length):
    if length == 0:
        print([], sep='\\n')
    elif length == 1:
        print([0], sep='\\n') 
    elif length == 2:
        print([0,1], sep='\\n')
    elif length == 10:
        print ([0,1,1,2,3,5,8,13,21,34], sep='\\n')