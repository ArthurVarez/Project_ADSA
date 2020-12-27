#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:40:31 2020

@author: Arthur
"""

import Module2



        
    
def HamiltonianPaths(graph, current, visited, path):

    if len(path) == len(graph.adj_matr):
    
        #Display a solution 
        print(path)
        return path

    # Check if every edge starting from current vertex leads to a solution or not
    for next_ in [graph.adj_matr[current].index[key] for key,value 
              in enumerate(graph.adj_matr[current]) if value ==1]:
        # here we get all the nieghbours possible representend in the adjacency 
        #matrix we defined in graph clas 


        # process only unvisited vertices as hamiltonian
        # path visits each vertex exactly once
        if next_ not in visited:
            visited.append(next_)
            path.append(next_)

            # check if adding vertex next_ to the path leads to solution or not
            HamiltonianPaths(graph, next_, visited, path)

            # Backtrack
            visited.remove(next_)
            path.pop()
    
    
def Hamilton_path_source(graph):
    #initialize the source for the previous resolving method 
    print("Choose your sources among the ones below  \n\n")
    sources = list(graph.keys())
    print(sources)
    start = input("\n\nChoice ? \n\n")

    path = [start]
    visited = list()
    visited.append(start)
    graph = Module2.Graph(map_crewmate)
    HamiltonianPaths(graph,start,visited,path)
    
    
    
    


if __name__=="__main__":
    # in this part we assume that we visit all the rooms of the maps
    # we do not have the informations of the remaining taksk on their locations
    # We will work with the same map(for creawmates) as we did in the Part 3
    path1 = 'map_crewmate.txt'
    map_crewmate =  map1=Module2.Get_Edges(
        Module2.Load_Graph(path1),
        Module2.Get_Vertice(Module2.Load_Graph(path1)))
    Hamilton_path_source(map_crewmate)
    #if nothing is display -> no solution 
    #In this part for respscting the original map of the game is named Amdmin and Comms
    # rooms, but if we do not we can have Hamilton paths for every source just 
    # but deleting th rooms of the graph. 
    # The problems with this rooms is that sometimes with have to cross Cafet
    # or Storage twice so We can have an hamilton path. 
    
    
   
    
   
    
   
    
   