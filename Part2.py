#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:07:55 2020

@author: Arthur
"""
import Module2 
from itertools import combinations
import random

def Get_SetImposters(graph):
    #get the vertices from the graph 
    vertices = set(graph.keys())
    # first suspected players 
    killers = [1,4,5]
    # get all the possible combinations with the killers 
    temp_=list(combinations(killers,2))
    
    imposters = list()
    
    # append to the posssible imposter set 
    for element in temp_:
        imposters.append(set(element))
    for element in killers:
        
        seen = set(graph[element])
        seen.add(element)
        # get the players the killers have not seen during the round 
        temp = set(vertices-seen)
        for e in temp:
           s = set([e,element])
           if s not in imposters:
               imposters.append(s)
            # append the sets of the players not seen by the current possible killers
    # set  here are needed to not get the same possible set 
    # exemple (1,5) and (5,1)        
    return imposters,len(imposters)


def Resolve_Coloring(graph):
    #initialization for the Colograph method and returning the res 
    col = {k:None for k in graph.keys()}
    current= list(graph.keys())[0]
    colors = ["blue","red","green","yellow"]
    col[current]=colors[random.randint(0,3)]
    return ColorGraph(graph,current,col)
    

def GetColors(graph,node,res,colors=["blue","red","green","yellow"]):
    # get the possible colors for a node cosidering its neighbours 
    neighbours = list(graph[node])
    temp_col=set()
    for element in neighbours:
        temp_col.add(res[element])
    return set(colors)-temp_col
    
def ColorGraph(graph,current,res,colors = ["blue","red","green","yellow"]):
    if all(element !=None for element in list(res.values())):
        # if all vertices has been well colored we can display them 
        # it's a solution
        print( res)
  
    if any(element == None for element in res.values()):
        
        for element in list(GetColors(graph,current,res)): #iterating into the list 
        # of possible colors 
            if element is not None:
                
                res[current]=element # affecting a color 
                
                
                next_ = str(int(current)+1)
            
                #backtracking 
                ColorGraph(graph, next_, res)
                res[current]=None
                
                
            
    
if __name__=="__main__":
    path = "graph.txt"
    l= Module2.Load_Graph(path)

    
    vertices = Module2.Get_Vertice(l)
    print(vertices)
    graph = Module2.Get_Edges_Unweighted(l,vertices)
    print(graph)
    print("Set of probable imposters : \n\n")
    
    g=Module2.ConvertGraphInt(graph)
    print(g)
    
    s = Get_SetImposters(g)
    print(s)
    Resolve_Coloring(graph)
    # if the color of one of the first predicted imposters is the same for an other 
    # players we have a solution 
    # exemple 4 is red and 8 is also red -> (4,8) is a solution of our problem