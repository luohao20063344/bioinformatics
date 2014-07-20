# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 10:27:43 2014

@author: dell
"""

import networkx as nx
import matplotlib.pyplot as plt

class myset(set):
    def __init__(self):
        self.e = 0

def read_genes(filename):
    mydict = {}
    with open(filename) as f:
        for line in f.readlines():
            mylist = line.strip().split()
            mydict[mylist[0]] = myset()
            mydict[mylist[0]].e = mylist[1]
    return mydict

def read_genes_new(filename):
    mydict = {}
    with open(filename) as f:
        for line in f.readlines():
            mylist = line.strip().split()
            mydict[mylist[0]] = mylist[1]
    return mydict

def read_binary_int(filename):
    edgeList = []
    with open(filename) as f:
        for line in f.readlines():
            binaryInt = line.strip().split()
            edgeList.append((binaryInt[0], binaryInt[1]))
            #entryList.append(binaryInt[0])
            #entryList.append(binaryInt[1])
    return edgeList

def get_binary_genes(mylist):
    geneList = []
    for item in mylist:
        geneList.append(item[0])
        geneList.append(item[1])
    return geneList

if __name__ == '__main__':
    
    mydict = read_genes_new('intact_genes.txt')
    edgeList_1 = read_binary_int('intact_binary.txt')
    
    genes_1 = set(mydict.keys())
    genes_2 = set(get_binary_genes(edgeList_1))
    
    geneSet = genes_1.intersection(genes_2)
    
    edgeList = filter(lambda x: x[0] in geneSet and x[1] in geneSet, edgeList_1)
    
    egList1 = filter(lambda x: x[0] in geneSet and x[1] == '1', mydict.items())
    negList1 = filter(lambda x: x[0] in geneSet and x[1] == '0', mydict.items())
    
    egList2 = list(zip(*egList1)[0])
    negList2 = list(zip(*negList1)[0])
        



    G = nx.Graph()
    G.add_edges_from(edgeList)
    G.add_nodes_from(egList2)
    G.add_nodes_from(negList2)
    #G.add_nodes_from(myGenes)
    position = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, position, nodelist = egList2, node_color = 'blue', node_size = 50, with_labels=False)
    nx.draw_networkx_nodes(G, position, nodelist = negList2, node_size = 50, with_labels=False)
    nx.draw_networkx_edges(G, position)
    #nx.draw_networkx(G, position, with_labels=False)
    plt.show()
    
    