# coding: utf-8
#
# Title:Perceptron
# Detail:margin
# Design:Naonori Nagano
# Date:2016/06/01
#

import sys
import random                                  # 2.9.1
random.seed(0)                                 # Random Number to 0
import numpy as np                             # 2.9.2

def read_instance(sent):                       # 2.8.1
    line = sent.strip().split()
    Tuple = []                                 # Tuple
    fv_index = []                              # FV-INDEX
    fv_count = []                              # FV-COUNT
    for word in line:
        if (word!=line[0]):                    # Not Label
            # Split (index:count)
            index,count = tuple(word.split(":"))
            # 2.9.2
            fv_index.append(index)             # ADD FV-INDEX
            fv_count.append(count)             # ADD FV-COUNT
    norm = np.linalg.norm(fv_count)            # Calculate norm
    # 2.9.3
    bias = (0,1)                               # bias(0,1)
    Tuple.append(bias)                         # ADD bias
    for j in range(len(fv_count)):
        x = float(fv_count[j]) / norm          # Calculate norm
        Tuple.append((fv_index[j],x))          # Input List
    LabelandFV = (line[0],Tuple)               # label & fv
    return LabelandFV

def read_data(data):                           # 2.8.2
    instance = []                              # Instance(All data)
    fv_max = 0                                 # feature-vector MAX
    # file-open
    for sent in open(data,"r").readlines():
        r_instance = read_instance(sent)       # read_instance
        instance.append(r_instance)
        # 2.8.3
        for fv in r_instance[1]:               # Input FV
            if int(fv[0]) > int(fv_max):       # Find FV-MAX
                fv_max = fv[0]                 # Input FV-MAX
    return instance,fv_max

def add_fv(fv):                                # 2.8.5
    for k in range(len(fv)):                   # Calculation
        # ADD weight+count(fv)
        weight[int(fv[k][0])] += float(fv[k][1])     

def sub_fv(fv):                                # 2.8.5
    for k in range(len(fv)):                   # Calculation
        # SUB weight+count(fv)
        weight[int(fv[k][0])] -= float(fv[k][1])

def mult_fv(fv):                               # 2.8.6
    ans = 0
    for k in range(len(fv)):                   # Calculation
        if len(weight) > int(fv[k][0]):        # Ignore over max_index
            # MULT weight*count(fv)
            ans += weight[int(fv[k][0])] * float(fv[k][1])
    return ans

def update_weight(fv):                         # 2.8.7&2.9.1
    random.shuffle(fv)                         # Shuffle Train-data
    for one_rev in fv:                         # Extract One review
        mult = mult_fv(one_rev[1])             # To MULT
        # Non-mutch weight*label(2.8.7) + weight*fv<=0.1(2.9.4)
        if (mult*int(one_rev[0])) <= 0.1:      # Condition for 2.9.4
            print(one_rev[0],mult)
            if int(one_rev[0]) > 0:            # Label is positive
                add_fv(one_rev[1])             # To ADD
            if int(one_rev[0]) < 0:            # Label is negative
                sub_fv(one_rev[1])             # To SUB

def evaluate(test_data):                       # 2.8.9
    correct = 0                                # Correct answer
    instance_count = 0                         # instance count
    for instance in test_data:                 # Extract One review
        instance_count += 1                    # Count instance
        mult = mult_fv(instance[1])            # To MULT
        if (mult*int(instance[0])) > 0:        # match weight*label
            correct += 1                       # count Correct answer
    rate = correct/instance_count              # Rate's of Correct answer
    return correct,instance_count,rate

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    # 2.8.8
    test_data, max_index_test = read_data(sys.argv[2])
    # weight(2.8.4)
    weight = [int(0)] * (int(max_index)+1)

    # 2.8.7&2.8.10
    for learning in range(int(sys.argv[3])):
        update_weight(train_data)

    # 2.8.9
    correct,instance_count,rate = evaluate(test_data)
    print("正解数："+str(correct))
    print("インスタンス数："+str(instance_count))
    print("正解率："+str(rate*100)+"%")
