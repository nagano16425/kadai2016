# coding: utf-8
#
# Title:Perceptron
# Detail:read_data
# Design:Naonori Nagano
# Date:2016/05/20
#

import sys

def read_instance(review):                 # 2.8.1
    line = review.strip().split()          # Input to List
    Tuple = []                             # Tuple
    label = line[0]                        # Extract label
    del line[0]                            # delete label
    Tuple = tuple(line)                    # Convert-tuple(Index:value)
    return label,Tuple

def read_data(data):                       # 2.8.2
    line = open(data,"r").readlines()      # file-opn
    instance = []                          # Instance(All data)
    for review in line:
        r_instance = read_instance(review) # read_instance
        instance.append(r_instance)
    return instance

if __name__=="__main__":
    print(read_data(sys.argv[1]))
