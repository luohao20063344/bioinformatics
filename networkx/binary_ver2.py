# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 09:42:54 2014

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 16:37:26 2014

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
    mydict = read_genes('intact_genes.txt')
    eList1 = read_binary_int('intact_binary.txt')
    
    geneSet = set(mydict.keys())
    geneList = get_binary_genes(eList1)
    
    myGenes = geneSet.intersection(set(geneList))
    
    #nodeList = filter(lambda x: x in myGenes, geneSet)
    edgeList = filter(lambda x: x[0] in myGenes and x[1] in myGenes, eList1)
    egList = []
    negList = []
    for item in myGenes:
        if mydict[item].e == '1':
            egList.append(item)
        elif mydict[item].e =='0':
            negList.append(item)
    egList1 = filter(lambda x: x[0] in myGenes and x[1].e == '1', mydict.items())
    #negList1 = filter(lambda x: x[0] in myGenes and x[1].e == '0', mydict.items())
    
    
    egList2 = list(zip(*egList1)[0])
    #negList = list(zip(*negList)[0])
        
    #G = nx.Graph()
    #G.add_edges_from(edgeList)
    #G.add_nodes_from(myGenes)
    #position = nx.spring_layout(G)
    #nx.draw_networkx_nodes(G, position, nodelist = egList, node_color = 'blue', node_size = 100)
    #nx.draw_networkx_nodes(G, position, nodelist = negList, node_size = 100)
    #nx.draw_networkx_edges(G, position)
    #nx.draw(G)
    #plt.show()

    