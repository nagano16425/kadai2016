# coding: utf-8
#
# Title:Perceptron
# Detail:max_index
# Design:Naonori Nagano
# Date:2016/05/20
#

import sys

def read_instance(i):                      # 2.8.1
    line = i.strip().split()               # Input to List
    Tuple = []                             # Tuple
    for j in line:
        if (j!=line[0]):                   # Not Label
            element = tuple(j.split(":"))  # Make Tuple
            Tuple.append(element)          # Input List
    LabelandFV = (line[0],Tuple)           # label & fv
    return LabelandFV

def read_data(data):                       # 2.8.2
    line = open(data,"r").readlines()      # file-opn
    instance = []                          # Instance(All data)
    fv_max = 0                             # feature-vector MAX
    for i in line:
        r_instance = read_instance(i)      # read_instance
        instance.append(r_instance)
        # 2.8.3
        for fv in r_instance[1]:           # Input FV
            if int(fv[0]) > int(fv_max):   # Find FV-MAX
                fv_max = fv[0]             # Input FV-MAX
    return instance,fv_max

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    weight = [0] * (int(max_index)+1)      # weight
    print(len(weight),weight)              # Confirm weight
