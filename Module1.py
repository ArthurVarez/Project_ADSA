#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:30:02 2020

@author: Arthur
"""


import random 
import Name
  

class Game:
    
    #For a caractrising a game we need players, a name, a rank and a status
    def __init__(self,name,Players=[],rank="No rank",status="In progress"):
        self.name=name
        self.Players=Players
        self.rank=rank
        self.status=status
        
    #Display a game 
    def __str__(self):
        res = "Name = {}, Rank = {}, Status = {} \n \nList of Players : \n\n".format(self.name, self.rank,self.status)
        for player in self.Players:
            res+=str(player)+"\n"
        return res
    
    #Methods to randomizes scores for differents rounds
    # Here I use a genrator to Have an independent experience evrytime I call
    #this method. 
    
    def RandomizeScores(self):
        if len(self.Players)!=0:
            for element in self.Players:
                element.val = random.randint(0, 12)
                
    def RandomizeScoreRound(self):
        if len(self.Players)!=0:
            for element in self.Players:
                element.val += (Name.generate_int()+Name.generate_int()+Name.generate_int())/3.0
    
    def RandomizeLastRound(self):
        if len(self.Players)!=0:
            for element in self.Players:
                element.val += (Name.generate_int()+
                                Name.generate_int()+
                                Name.generate_int()+
                                Name.generate_int()+
                                Name.generate_int())/5.0
      
    #method to change the status of the game, asking an input from the user.
    def EndTheGame(self):
        choice = input("Do you want to end the Game {} ?(yes/no) \n".format(self.name))
        if choice in ['yes','no']:
            if choice == 'yes':
                self.status="Ended"
                print("Game ended")
            


                
            
                