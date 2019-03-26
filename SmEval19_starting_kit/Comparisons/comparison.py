#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:34:33 2019

@author: shanedaly
"""

import numpy as np
import pandas as pd

goldStandard = "gold_standard.tsv"
outputFile = "results.txt"

gold = []
output = []

def read_csv(filename):
    # read in file
    data = pd.read_csv(filename, delimiter="\t")
    standard = data.values
    return standard

def read(filename):
    results = np.loadtxt(filename)
    return results

def compare_hs(gold, output):
    
    f1Score = 0.0
    microAcc = 0.0
    accuracy = 0.0
    
    correct_classifications = 0
    if gold[2] == 1 and output[2] == 'HS':
        correct_classifications += 1
    elif gold[2] == 0 and output[2] == 'OK':
        correct_classifications += 1
    else: 
        pass
    
    accuracy = correct_classifications/len(gold)
    
def compare_tg():
    pass

def compare_ag():
    pass


gold_data = read_csv(goldStandard)
output_data = read(outputFile)