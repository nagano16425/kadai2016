# coding: utf-8
#
# Title:Perceptron
# Detail:Averaging Perceptron
# Design:Naonori Nagano
# Date:2016/06/14
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

def add_fv(fv,weight):                         # 2.8.5
    for k in range(len(fv)):                   # Calculation
        # ADD weight+count(fv)
        weight[int(fv[k][0])] += float(fv[k][1])     
    return weight

def sub_fv(fv,weight):                         # 2.8.5
    for k in range(len(fv)):                   # Calculation
        # SUB weight+count(fv)
        weight[int(fv[k][0])] -= float(fv[k][1])
    return weight

def mult_fv(fv,weight):                        # 2.8.6
    ans = 0
    for k in range(len(fv)):                   # Calculation
        if len(weight) > int(fv[k][0]):        # Ignore over max_index
            # MULT weight*count(fv)
            ans += weight[int(fv[k][0])] * float(fv[k][1])
    return ans

def update_weight(fv,nupdates):                # 2.8.7 & 2.9.1 & 2.9.5
    random.shuffle(fv)                         # Shuffle Train-data
    for one_rev in fv:                         # Extract One review
        mult = mult_fv(one_rev[1],weight)      # To MULT
        # Non-mutch weight*label(2.8.7) + weight*fv<=0.1(2.9.4)
        if (mult*int(one_rev[0])) <= 0.1:      # Condition for 2.9.4
            if int(one_rev[0]) > 0:            # Label is positive
                add_fv(one_rev[1],weight)      # To ADD
            if int(one_rev[0]) < 0:            # Label is negative
                sub_fv(one_rev[1],weight)      # To SUB
            nupdates += 1                      # update nupdates
            # 2.9.5
            x = []
            for element in one_rev[1]:
                index,count = element          # Split Index:Count
                # Append index & count(count*nupdates)
                x.append((index,float(count)*int(nupdates)))
            if int(one_rev[0]) > 0:            # Label is positive
                add_fv(x,weight)               # To ADD
            if int(one_rev[0]) < 0:            # Label is negative
                sub_fv(x,weight)               # To SUB
    averaged_weight(fv,nupdates)               # To Averaged weight
    return weight,tmp_weight,nupdates

def evaluate(test_data,weight):                # 2.8.9 & 2.9.8
    correct = 0                                # Correct answer
    instance_count = 0                         # instance count
    print(weight)
    for instance in test_data:                 # Extract One review
        instance_count += 1                    # Count instance
        mult = mult_fv(instance[1],weight)     # To MULT
        if (mult*int(instance[0])) > 0:        # match weight*label
            correct += 1                       # count Correct answer
    rate = correct/instance_count              # Rate's of Correct answer
    return correct,instance_count,rate

def averaged_weight(fv,nupdates):              # 2.9.6 & 2.9.7
    ave_weight = []
    if not len(weight) == len(tmp_weight):     # Non match
        print("Failed!!")
    if len(weight) == len(tmp_weight):         # Match
        for i in range(len(weight)):
            # weight-(tmp_weight/(nupdates+1))
            x = weight[i] - tmp_weight[i] / (int(nupdates)+ 1)
            ave_weight.append( x )             # Append Averaged_weight
        # print("Success!!")
    return ave_weight

if __name__=="__main__":
    # 2.8.4
    train_data, max_index = read_data(sys.argv[1])
    # 2.8.8
    test_data, max_index_test = read_data(sys.argv[2])
    # weight(2.8.4) & tmp_weight(2.9.5)
    weight = [int(0)] * (int(max_index)+1)
    tmp_weight = weight

    # 2.8.7 & 2.8.10 & 2.9.5 & 2.9.8
    nupdates = 0
    for learning in range(int(sys.argv[3])):
        weight,tmp_weight,nupdates = update_weight(train_data,nupdates)

    # 2.8.9 & 2.9.8
    correct,instance_count,rate = evaluate(test_data,weight)
    print("重み更新回数："+str(nupdates))
    print("正解数："+str(correct))
    print("インスタンス数："+str(instance_count))
    print("正解率："+str(rate*100)+"%")
