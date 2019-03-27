#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:34:33 2019

@author: shanedaly
"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

goldStandard = "gold_standard.tsv"
hs = "hs.txt"
tg = "tg.txt"
ag = "ag.txt"

gold = []
output = []

def read_csv(filename):
    # read in file
    data = pd.read_csv(filename, delimiter="\t")
    standard = data.values
    return standard    

def compare_hs(gold, output):
    print("------- HS ------")
    f1Score = 0.0
    accuracy = 0.0
    precision = 0.0
    
    actual = []
    predicted = []
    correct = 0
    
    for x in range(0,len(gold)):
        actual.append(gold[x][2])
        if output[x][2] == 'HS':
            predicted.append(1)
        else:
            predicted.append(0)
    
    # Accuracy Of Model
    for i in range(0, len(predicted)):
        if actual[i] == predicted[i]:
            correct += 1
    
    print("Confusion Matrix")
    print(confusion_matrix(actual, predicted))
    
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)
    
    # True Positives
    TP = np.sum(np.logical_and(predicted == 1, actual == 1))
    #True Negatives
    TN = np.sum(np.logical_and(predicted == 0, actual == 0))
    #False Positives
    FP = np.sum(np.logical_and(predicted == 1, actual == 0))
    #False Negatives
    FN = np.sum(np.logical_and(predicted == 0, actual == 1))
    
    accuracy = correct/len(actual)
    print("\nAccuracy: ", accuracy)
    
    precision = TP/(TP+FP)
    print("Precision: ", precision)
    
    recall = TP/(TP+FN)
    print("Recall: ", recall)
    
    f1Score = (2*precision*recall)/(precision/recall)
    print("F1: ", f1Score)
    
    
def compare_tg(gold, output):
    print("\n------- TG ------")
    f1Score = 0.0
    accuracy = 0.0
    precision = 0.0
    
    actual = []
    predicted = []
    correct = 0
    
    for x in range(0,len(gold)):
        actual.append(gold[x][3])
        if output[x][2] == 'TG':
            predicted.append(1)
        else:
            predicted.append(0)
    
    # Accuracy Of Model
    for i in range(0, len(predicted)):
        if actual[i] == predicted[i]:
            correct += 1
    
    print("Confusion Matrix")
    print(confusion_matrix(actual, predicted))
    
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)
    
    # True Positives
    TP = np.sum(np.logical_and(predicted == 1, actual == 1))
    #True Negatives
    TN = np.sum(np.logical_and(predicted == 0, actual == 0))
    #False Positives
    FP = np.sum(np.logical_and(predicted == 1, actual == 0))
    #False Negatives
    FN = np.sum(np.logical_and(predicted == 0, actual == 1))
    
    accuracy = correct/len(actual)
    print("\nAccuracy: ", accuracy)
    
    precision = TP/(TP+FP)
    print("Precision: ", precision)
    
    recall = TP/(TP+FN)
    print("Recall: ", recall)
    
    f1Score = (2*precision*recall)/(precision/recall)
    print("F1: ", f1Score)

def compare_ag(gold, output):
    print("\n------- AG ------")
    f1Score = 0.0
    accuracy = 0.0
    precision = 0.0
    
    actual = []
    predicted = []
    correct = 0
    
    for x in range(0,len(gold)):
        actual.append(gold[x][4])
        if output[x][2] == 'AG':
            predicted.append(1)
        else:
            predicted.append(0)
    
    # Accuracy Of Model
    for i in range(0, len(predicted)):
        if actual[i] == predicted[i]:
            correct += 1
    print("Confusion Matrix")
    print(confusion_matrix(actual, predicted))
    
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)
    
    # True Positives
    TP = np.sum(np.logical_and(predicted == 1, actual == 1))
    #True Negatives
    TN = np.sum(np.logical_and(predicted == 0, actual == 0))
    #False Positives
    FP = np.sum(np.logical_and(predicted == 1, actual == 0))
    #False Negatives
    FN = np.sum(np.logical_and(predicted == 0, actual == 1))
    
    accuracy = correct/len(actual)
    print("\nAccuracy: ", accuracy)
    
    precision = TP/(TP+FP)
    print("Precision: ", precision)
    
    recall = TP/(TP+FN)
    print("Recall: ", recall)
    
    f1Score = (2*precision*recall)/(precision/recall)
    print("F1: ", f1Score)

# Hate Speech Model. 
gold_data = read_csv(goldStandard)
output_data = read_csv(hs)
compare_hs(gold_data, output_data)

# Targeted Model
tg_data = read_csv(tg)
compare_tg(gold_data, tg_data)

# Aggression Model
ag_data = read_csv(ag)
compare_ag(gold_data, ag_data)