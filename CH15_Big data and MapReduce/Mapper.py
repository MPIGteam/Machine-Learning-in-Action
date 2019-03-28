#!/usr/bin/env python
#coding=utf-8

import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.rstrip()
input = read_input(sys.stdin)
input = [float(line) for line in input]
#print(input,'=====')
numInputs = len(input)
input = mat(input)
sqInput = power(input, 2)

print ("%d\t%f\t%f" % (numInputs, mean(input), mean(sqInput)) ) # calc mean of columns
#print (  sys.stderr, "report: still alive" )