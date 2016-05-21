# coding: utf-8
#
# Title:Perceptron
# Detail:read_instance
# Design:Naonori Nagano
# Date:2016/05/20
#

import sys

def read_instance(data):
    fv = []                            # Feature-vector
    for review in data:
        line = review.strip().split()  # Input to List
        label = tuple(line[0])         # Convert-tuple(label)
        del line[0]                    # delete label
        fv = tuple(line)               # Convert-tuple(Index:value)
        # Output
        print(label)
        print(fv)
    return

if __name__=="__main__":
    # input
    data = open(sys.argv[1]).readlines()
    # read_instance
    read_instance(data)
