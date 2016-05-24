# coding: utf-8
#
# Title:Perceptron
# Detail:mult_fv
# Design:Naonori Nagano
# Date:2016/05/24
#

import sys

def read_instance(i):                          # 2.8.1
    line = i.strip().split()                   # Input to List
    Tuple = []                                 # Tuple
    for j in line:
        if (j!=line[0]):                       # Not Label
            element = tuple(j.split(":"))      # Make Tuple
            Tuple.append(element)              # Input List
    LabelandFV = (line[0],Tuple)               # label & fv
    return LabelandFV

def read_data(data):                           # 2.8.2
    line = open(data,"r").readlines()          # file-opn
    instance = []                              # Instance(All data)
    fv_max = 0                                 # feature-vector MAX
    for i in line:
        r_instance = read_instance(i)          # read_instance
        instance.append(r_instance)
        # 2.8.3
        for fv in r_instance[1]:               # Input FV
            if int(fv[0]) > int(fv_max):       # Find FV-MAX
                fv_max = fv[0]                 # Input FV-MAX
    return instance,fv_max

def add_fv(fv):                                # 2.8.5
    for v in fv:                               # Extract fv
        for k in v[1]:                         # Extract count(fv)
            weight[int(k[0])] += int(k[1])     # ADD weight+count(fv)

def sub_fv(fv):                                # 2.8.5
    for v in fv:                               # Extract fv
        for k in v[1]:                         # Extract count(fv)
            weight[int(k[0])] -= int(k[1])     # SUB weight-count(fv)

def mult_fv(fv):                               # 2.8.6
    if not len(weight) < len(fv):              # Ignore over max_index
        for v in fv:                           # Extract fv
            for k in v[1]:                     # Extract count(fv)
                weight[int(k[0])] *= int(k[1]) # MULT weight*count(fv)

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    weight = [int(0)] * (int(max_index)+1)      # weight

    # 2.8.5 & 2.8.6
    # add_fv(train_data)
    # sub_fv(train_data)
    mult_fv(train_data)
    print(weight)
