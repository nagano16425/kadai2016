#!/bin/sh
#
# HOW TO USE
# Command:bash perceptron.sh (update)
#
 
# Normal
python3 perceptron.py -u $1> $1.csv
# B
python3 perceptron.py -u $1 -b >> $1.csv
# BN
python3 perceptron.py -u $1 -b -n >> $1.csv
# BM
python3 perceptron.py -u $1 -b -m 0.1 >> $1.csv
# BA
python3 perceptron.py -u $1 -b -a >> $1.csv
# BNM
python3 perceptron.py -u $1 -b -n -m 0.1 >> $1.csv
# BNA
python3 perceptron.py -u $1 -b -n -a>> $1.csv
# BMA
python3 perceptron.py -u $1 -b -m 0.1 -a >> $1.csv
# BNMA
python3 perceptron.py -u $1 -b -n -m 0.1 -a >> $1.csv
# N
python3 perceptron.py -u $1 -n >> $1.csv
# NM
python3 perceptron.py -u $1 -n -m 0.1 >> $1.csv
# NA
python3 perceptron.py -u $1 -n -a >> $1.csv
# NM
python3 perceptron.py -u $1 -n -m 0.1 -a >> $1.csv
# M
python3 perceptron.py -u $1 -m 0.1 >> $1.csv
# MA
python3 perceptron.py -u $1 -m 0.1 -a >> $1.csv
# A
python3 perceptron.py -u $1 -a >> $1.csv