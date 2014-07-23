# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 10:01:41 2014

@author: dell
"""

import pandas as pd

if __name__ == '__main__':
    df = pd.read_table('binary_intact.txt', header = None)
    #for item in df.get_values(): # df.values
    
    # read essential genes and non-essential genes
    egFile = pd.read_table('source_1_eg.tab')
    negFile = pd.read_table('source_1_neg.tab')
    egList_1 = []
    negList_1 =[]
    for item in egFile.values:
        egList_1.append(item[1])
    for item in negFile.values:
        negList_1.append(item[1])
    
    # find the binary interactor proteins of genes
    # eg: a = df[df[0] == 'P16655']
    row_list = []
    for item in set(egList_1):
        a = df[df[0] == item]
        b = df[df[1] == item]
        c = set(a[1]).union(b[0])
        mydict = {'entry':item, 'essential':1, 'length':len(c), 'item':' '.join(list(c))}
        row_list.append(mydict)
    mydf = pd.DataFrame(row_list)
    
    mydf.to_csv('eg.csv')
    
    row_list = []
    for item in set(negList_1):
        a = df[df[0] == item]
        b = df[df[1] == item]
        c = set(a[1]).union(b[0])
        mydict = {'entry':item, 'essential':1, 'length':len(c), 'item':' '.join(list(c))}
        row_list.append(mydict)
    mydf = pd.DataFrame(row_list)
    mydf.to_csv('neg.csv')
    #a = mydf.to_html()
    #with open('test.html','w') as f:
    #    print >> f, a
    #b = mydf.to_clipboard()
        
    #mydf = {'entry':[], 'essential':[], 'length':[]}
    #frame = pd.DataFrame(mydf)
    #mydf = pd.DataFrame(columns = ('a1', 'a2', 'a3'))
    #row = pd.DataFrame([{'a1':1, 'a2':1, 'a3':1}])
    #row = pd.DataFrame([{'a1':1, 'a2':1, 'a3':1},{'a1':1, 'a2':1, 'a3':1}])
    #mydf = mydf.append(row, ignore_index = True)