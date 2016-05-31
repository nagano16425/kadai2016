# coding: utf-8
#
# Title:Perceptron
# Detail:update_weight
# Design:Naonori Nagano
# Date:2016/05/25
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
    for k in range(len(fv)):                   # Calculation
        # ADD weight+count(fv)
        weight[int(fv[k][0])] += int(fv[k][1])     

def sub_fv(fv):                                # 2.8.5
    for k in range(len(fv)):                   # Calculation
        # SUB weight+count(fv)
        weight[int(fv[k][0])] -= int(fv[k][1])

def mult_fv(fv):                               # 2.8.6
    ans = 0
    for k in range(len(fv)):                   # Calculation
        if not len(weight) < len(fv):          # Ignore over max_index
            # MULT weight*count(fv)
            ans += weight[int(fv[k][0])] * int(fv[k][1])
    return ans

def update_weight(fv):                         # 2.8.7
    for one_rev in fv:                         # Extract One review
        mult = mult_fv(one_rev[1])             # To MULT
        if (mult*int(one_rev[0])) <= 0:        # Non-mutch weight*label
            if int(one_rev[0]) > 0:            # Label is positive
                print(mult,one_rev[0])         # check 2.8.7
                print("add")                   # check 2.8.7
                add_fv(one_rev[1])             # To ADD
            else:                              # Label is negative
                print(mult,one_rev[0])         # check 2.8.7
                print("sub")                   # check 2.8.7
                sub_fv(one_rev[1])             # To SUB

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    weight = [int(0)] * (int(max_index)+1)      # weight

    # 2.8.7
    update_weight(train_data)
