# coding: utf-8
#
# Title:Perceptron
# Detail:addsub_fv
# Design:Naonori Nagano
# Date:2016/05/24
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

def add_fv(fv):                            # 2.8.5
    for k in range(len(fv)):               # Calculation
        # ADD weight+count(fv)
        weight[int(fv[k][0])] += int(fv[k][1])     

def sub_fv(fv):                            # 2.8.5
    for k in range(len(fv)):               # Calculation
        # SUB weight+count(fv)
        weight[int(fv[k][0])] -= int(fv[k][1])

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    weight = [int(0)] * (int(max_index)+1)      # weight

    # 2.8.5
    for one_rev in train_data:
        # add_fv(one_rev[1])
        sub_fv(one_rev[1])
    print(weight)
