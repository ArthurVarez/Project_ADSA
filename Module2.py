#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:16:08 2020

@author: Arthur
"""

import pandas as pd


class Graph(object):
    #Vertices are the keys and edges the values corresponding 
    def __init__(self,graph):
        self.adj_matr = pd.DataFrame(0, columns=graph.keys(), index=graph.keys())
        #cretaing the dataframe with the names of the rooms as columns and indexes 
        for key in graph.keys():
            for element in graph[key].keys():
                #filling this dataframe with 1 if rooms a connected
                self.adj_matr[key][element]=1
                self.adj_matr[element][key]=1
                
                            
                
def Load_Graph(path):
    # reading the file ansd returning a list of list 
    list_graph= list()
    f = open(path)
    for line in f:
        temp= line.strip().split(" ")
        list_graph.append(temp)
    return list_graph


def Get_Vertice(list_graph):
    edges = set()
    #get the first elements of the Load_Graph method a creating a set to 
    #grap all the element possible
    for element in list_graph:
        edges.add(element[0])
    return sorted(edges)

def Get_Edges(list_graph,vertices):
    #creating a dictionnaire with vertices as keys
    graph = {element:dict() for element in vertices}
    for element in list_graph:
        #setting corresping edges with the weight 
        graph[element[0]][element[1]]=int(element[2])
        
    return graph

def Get_Edges_Unweighted(list_graph,vertices):
    #Same as above but without weigh for edges
    graph = {element:set() for element in vertices}
    for element in list_graph:
        graph[element[0]].add(element[1])
        
    return graph

def ConvertGraphInt(g):
    #convert the graph element as int type 
    new_graph={int(element) : set() for element in g.keys()}
    for key,value in g.items():
        new_graph[int(key)]= [int(a) for a in value]
    return new_graph
    


