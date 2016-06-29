# coding: utf-8
#
# Title:Perceptron
# Detail:perceptron(extend)
# Design:Naonori Nagano
# Date:2016/06/14
#

import sys
import random                                  # 2.9.1
random.seed(0)                                 # Random Number to 0
import numpy as np                             # 2.9.2
from optparse import OptionParser              # 2.9.9

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
    # 2.9.9
    if(options.normalize==True):               # normalize option is "True"
        norm = np.linalg.norm(fv_count)        # Calculate norm
    else:                                      # normalize option is "False"
        norm = 1                               # Non Calucuate norm
    # 2.9.3 & 2.9.9
    if(options.bias==True):                    # bias option is "True"
        bias = (0,1)                           # bias(0,1)
        Tuple.append(bias)
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
        abs_mult = abs(mult)                   # MULT(Absolute value)
        # Non-mutch weight*label(2.8.7) + weight*fv<=margin(2.9.9)
        if (mult*int(one_rev[0]) <= 0 or abs_mult <= options.margin):
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
                add_fv(x,tmp_weight)           # To ADD
            if int(one_rev[0]) < 0:            # Label is negative
                sub_fv(x,tmp_weight)           # To SUB
    # 2.9.9
    if(options.average==True):                 # average option is "True"
        # To Averaged weight
        ave_weight = averaged_weight(fv,nupdates)
    else:
        # Instead of Averaged weight
        ave_weight = []
    return weight,tmp_weight,nupdates,ave_weight

def evaluate(test_data,weight):                # 2.8.9 & 2.9.8
    correct = 0                                # Correct answer
    instance_count = 0                         # instance count
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
    # 2.9.9(OptionParser)
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)
    parser.add_option(
        "-u","--updates",
        dest="updates",default="1",type="int",help="Number of Updates")
    parser.add_option(
        "-b","--bias",
        dest="bias",default="False",action="store_true",help="Set Bias Terms")
    parser.add_option(
        "-n","--normalize",
        dest="normalize",default="False",action="store_true",help="To Normalize the L2 Norm")
    parser.add_option(
        "-m","--margin",
        dest="margin",default="0",type="float",help="Set the margin")
    parser.add_option(
        "-a","--average",
        dest="average",default="False",action="store_true",help="Evaluate by Averaged weight")
    (options, args) = parser.parse_args()
    print(options)

    # 2.8.4
    train_data, max_index = read_data("train_cv0.txt")
    # 2.8.8
    test_data, max_index_test = read_data("test_cv0.txt")
    # weight(2.8.4) & tmp_weight(2.9.5)
    weight = [int(0)] * (int(max_index)+1)
    tmp_weight = weight

    # 2.8.7 & 2.8.10 & 2.9.5 & 2.9.8 & 2.9.9
    nupdates = 0
    for learning in range(options.updates):
        weight,tmp_weight,nupdates,ave_weight = update_weight(train_data,nupdates)

    # 2.8.9 & 2.9.8 & 2.9.9
    if(options.average==True):                 # average option is "True"
        correct,instance_count,rate = evaluate(test_data,ave_weight)
    else:
        correct,instance_count,rate = evaluate(test_data,weight)
    print("Update Weight：" +"\t"+","+str(nupdates))
    print("Correct Answer："+"\t"+","+str(correct))
    print("Instance Count："+"\t"+","+str(instance_count))
    print("Correct Rate："  +"\t"+","+str(rate*100)+","+"%")
