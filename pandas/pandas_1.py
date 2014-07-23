# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 14:14:56 2014

@author: dell
"""
import pandas as pd

def output_GeneSet(eglist, neglist):
    with open('geneSet.txt', 'w') as f:
        for item in set(eglist):
            print >> f, '%s\t1' % item
        for item in set(eglist):
            print >> f, '%s\t0' % item
def findEntry(dataframe, entry, columns):
    query = 'uniprotkb:' + entry
    return dataframe[dataframe[columns] == query]

if __name__ == '__main__':
    egFile = pd.read_table('source_1_eg.tab')
    negFile = pd.read_table('source_1_neg.tab')
    egList_1 = []
    negList_1 =[]
    for item in egFile.values:
        egList_1.append(item[1])
    for item in negFile.values:
        negList_1.append(item[1])
    #output_GeneSet(egList_1, negList_1)
    
    #df = pd.read_table('../intact-micluster.txt')
    #tp = findEntry(df, 'P02394', 'Alt. ID(s) interactor B')
    #tp.to_csv('test2.csv', header = False, mode = 'a')
    #tp1 = findEntry(df, 'P37550', 'Alt. ID(s) interactor B')
    egList = set(egList_1)
    negList = set(negList_1)

    if False:
        df = pd.read_table('../intact-micluster.txt')
        for item in egList:
            tp = findEntry(df, item, 'Alt. ID(s) interactor B')
            tp.to_csv('test_eg.csv', header = False, mode = 'a')
        for item in negList:
            tp = findEntry(df, item, 'Alt. ID(s) interactor B')
            tp.to_csv('test_neg.csv', header = False, mode = 'a')
    