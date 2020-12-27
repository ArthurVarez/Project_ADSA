#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:36:01 2020

@author: Arthur
"""
import random
from Module1 import Game
from Database import AVL_Tree
import Name

def Populate_DB(DB):#Our Database is empty here
    root =None
    for i in range(1,101):
        val=0.0
        #val = float(Name.generate_int()) -> if you want to fill it with non null values
        root = DB.insert(root,val,'Player{}'.format(i))
    DB.root=root
        

def Delete_Last10(db):
    #grab the list of players and sort them by scores
    elements = db.InOrder_List(db.root)
    elements = sorted(elements, key = lambda x:x.val,reverse=True)[:len(elements)-10]
    #print(len(elements))
    #input("pause")
    #new Database
    Dbtemp = AVL_Tree()
    root=None
    for e in elements:
        #Insert into the new database 
        root = Dbtemp.insert(root,e.val,e.name)
    Dbtemp.root=root
    return Dbtemp


def Play_Until10(DB):
    # because the length of the DB is 100 we need to occurr 9 times 
    for i in range(9):
        if i ==0:
            #First round need to be random 
            Play1stRound(DB)
            DB=Delete_Last10(DB)
        else:
            #After the round there's a ranking 
            Play_Ranking_Round(DB)
            DB=Delete_Last10(DB)
    #In the end of both loops we need to update the DB
    return DB
                 
    
    
def CreateRandomGame(db):
    if isinstance(db, AVL_Tree):
        # we want the players of our DB 
        d = db.InOrder_List(db.root)
    else:
        d =db 
    if len(d)<10:
        print("Not enough Players in DB to create a game")
    else:
        #Create the set to select random Players
        s = set()
        
        n = len(d)-1
        
        while len(s)<10:
            # Random selection 
            i = random.randint(0, n)
            #Because s is a set 
            #->no int doublons 
            s.add(i)
        temp = list()
        
        for element in s:
            #then we create our list of players 
            temp.append(d[element])
        name = Name.generate_word(6) #generate a random name
        game = Game(name,temp)
        return game
    

def Play1stRound(db):
    d = db.InOrder_List(db.root)
    #for the first games we need to randomize because players have a 
    #score of 0
    
    games =list()
    while len(d)!=0:
        g= CreateRandomGame(d)
        
        games.append(g)
        #Delete the players already playing
        for p in g.Players:
            d.remove(p)
        
            
    # we randomize the scores for the round 
    for game in games : 
        game.RandomizeScoreRound()
        
        
    return games # returning our collection of games 


def PlayLastRound(DB):
    # Last round -> 5 games with rank 1 
    for element in DB.InOrder_List(DB.root):
        element.val = 0
    if len(DB.InOrder_List(DB.root))==10:
        final=CreateRankingGame(DB,'Rank1')
        final.RandomizeLastRound()
    return final


def Display_Podium(game):
    podium = dict()
    # our 3 best players 
    top_players = sorted(game.Players, key = lambda x : x.val,reverse=True)[:3]
    podium["Winner"] = str(top_players[0])
    podium["2nd"] = str(top_players[1])
    podium["3rd"] = str(top_players[2])
    print("Here is the podium of the tournament : \n \n")
    for k,v in podium.items():
        #display them 
        print("{} , {} \n\n".format(k,v))
       
    
#method to play ranking rounds 
def Play_Ranking_Round(db):
    d = db.InOrder_List(db.root)
    games = list()
    e = len(d)//10 # our counter dor ranks 
    while len(d)!=0: # if len(d)!= 0 -> not all players have been affetcted to a game 
        g = CreateRankingGame(d,"Rank{}".format(e))
        games.append(g)
        e-=1
        for p in g.Players:
            d.remove(p)
            #remove the players already affected to a game 
    for game in games:
        game.RandomizeScoreRound()
        # randomize scores 
    return games 

        
def CreateRankingGame(db,rank,name=None):
    if isinstance(db,AVL_Tree):
        d = db.InOrder_List(db.root)
    else:
        d = db
    ranks = GetRanks(d) # get the posssible ranks for the db considering its state
    # with the players corresponding 
    
    #list of  players for the given rank 
    players= ranks[rank]
    #create the game
    if name == None:
        name=Name.generate_word(6)
    game = Game(name,players,rank)
    return game

def GetRanks(db):

    #firtly we have to sort the database by score of the players
    dbtemp = sorted(db,key=lambda player:player.val,reverse=True)
    ranks = dict()
    count =1 #int to have a classification of ranks (rank1->10 best players)
    for i in range(0,len(db)-1,10):
        ranks["Rank{}".format(count)]=dbtemp[i:i+10]
        count+=1
    # return the dict for players corresping to their rank.
    return ranks

if __name__=='__main__':
    Database = AVL_Tree()
    Populate_DB(Database)
    Database=Play_Until10(Database)
    print("Here are the 10 last Players : \n")
    print("------------------------------------------------------\n")
    print("------------------------------------------------------\n")
    Database.InOrder(Database.root)
    print("\n------------------------------------------------------\n")
    print("\n------------------------------------------------------\n")
    final_game=PlayLastRound(Database)
    final_game.EndTheGame()
    print("\naverage results of the final games : \n ")
    print(str(final_game))
    Display_Podium(final_game)
    
    
    
    
    
    
  
    
   
    
    
        

    
        
   
    

