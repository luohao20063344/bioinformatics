# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:56:41 2014

@author: dell
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
nodeList = [0,1,2,3,4,5]
edgeList = [(0,1), (2,3),(3,4),(1,4), (2,5), (0,4)]
G.add_nodes_from(nodeList)
G.add_edges_from(edgeList)
G.edge[2][3]['mylebel'] = 'essential'
pos = nx.spring_layout(G)

edge_labels = nx.get_edge_attributes(G, 'mylebel')
nx.draw_networkx_nodes(G, pos, nodelist = [2,3], node_color = 'blue')
nx.draw_networkx_nodes(G, pos, nodelist = [0,1,4,5])

nx.draw_networkx_edges(G, pos)

#nx.draw_networkx_labels(G, pos, lebels = edge_labels)
plt.show()