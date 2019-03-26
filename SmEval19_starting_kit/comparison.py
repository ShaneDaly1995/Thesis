#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:34:33 2019

@author: shanedaly
"""

goldStandard = ""
outputFile = ""

gold = []
output = []

def read():
    # read in file
    pass

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