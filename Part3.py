#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:46:55 2020

@author: Arthur
"""

from itertools import combinations

import Module2

def TimeToTravel(graph):
    vertices = list(graph.keys())
    pairs = list(combinations(vertices,2)) # get all the combinaisons of paths
    #between two rooms 
    res =  list()
    for element in pairs:
        a= Dijkstra(graph.copy(),element[0],element[1])[0]
        # the print above is to skip the displays when using the TimeDifference
        #function, if you want to see the results of this one, just unquote 
        #the line under this one (Dont forget to quote it again or it will be 
        #hard to reed the print of the funnction under ;))
        """print("Time to travel between {} and {} : {} secondes".format(
            element[0],element[1],a))"""
        res.append((element[0],element[1],a))
    return res 
        
    
def TimeDifference(graph1,graph2):
    times_map1cm, timesmapimp = TimeToTravel(graph1),TimeToTravel(graph2)
    # we take the shortest paths for all pairs of room for each map
    
    # now we can calculate the diffenrence tge diffenrence and display the results 
    for i in range(len(times_map1cm)):
        print(
            " difference of time to travel between {} and {} : {} secondes".format(
                times_map1cm[i][0],times_map1cm[i][1]
                ,abs(times_map1cm[i][2]-timesmapimp[i][2])))
        

def Dijkstra(graph,start,end):
    shortest_distance = dict()
    parents = dict()
    to_visit = graph
    inf = 10000
    path = list()
    for element in to_visit:
        # we assume that no element can we reached for the first step 
        shortest_distance[element] = inf
    shortest_distance[start] = 0
    
    while to_visit:
        min_distance = None
        for element in to_visit:
            if min_distance is  None:
                # we set a possible path 
                min_distance= element
            if shortest_distance[element]< shortest_distance[min_distance]:
                # if not the shortest with take an other 
                min_distance = element
        paths = graph[min_distance].items()
        
        for child,weight in paths:
            if weight + shortest_distance[min_distance] < shortest_distance[child]:
                shortest_distance[child] = weight+ shortest_distance[min_distance]
                parents[child] = min_distance
        to_visit.pop(min_distance)
    node = end
    
    while node!=start:
        path.insert(0,node)
        node = parents[node]
    
    path.insert(0,start)
    
        
    return shortest_distance[end], path
                
                

if __name__ == '__main__':
    path1 ="map_crewmate.txt"
    path2 = "map_imposter.txt"
    
    map1=Module2.Get_Edges(
        Module2.Load_Graph(path1),
        Module2.Get_Vertice(Module2.Load_Graph(path1)))
    map2=Module2.Get_Edges(
        Module2.Load_Graph(path2),
        Module2.Get_Vertice(Module2.Load_Graph(path2)))
    TimeToTravel(map1)
    TimeToTravel(map2)
    TimeDifference(map1,map2)
    
   
    
        
