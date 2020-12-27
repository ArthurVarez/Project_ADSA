#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:30:02 2020

@author: Arthur
"""

#CLass node for the Avl Tree i will use as a database 

class Player_Node(object):
    
    def __init__(self,value,name):
        self.val=value #score of the player
        self.name=name # its namem 
        self.left = None # left child 
        self.right=None # right child 
        self.height = 1 # height of the node 
        
        
    def __str__(self):
        return "Name : {}, score : {}".format(self.name,self.val)
    
    def __eq__(self, o):
        if isinstance(o,Player_Node):
            return self.name==o.name and self.val == o.val
        
class AVL_Tree(object):
    
    def __init__(self,root = None):
        self.root=root
        
    def insert(self, root, key_value,key_name): 
	
		#inserting the futur node by using recursion
        if not root: 
            return Player_Node(key_value,key_name) 
        
        elif key_name < root.name: 
            root.left = self.insert(root.left, key_value,key_name) 
            
        else: 
            root.right = self.insert(root.right, key_value,key_name) 

        #check if the tree is balanced, if not : Whats rotaion to perform to rebalence?
        root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 
        balance = self.getBalance(root) 
        
        #Rebalancing using rotation methods
        if balance > 1 and key_name < root.left.name: 
            return  self.rightRotate(root) 

        if balance < -1 and key_name > root.right.name: 
            return self.leftRotate(root) 

        if balance > 1 and key_name > root.left.name: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        if balance < -1 and key_name < root.right.name: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 



    # the two function below is to perform rotation to balance the tree 
    # when performing operation on it. 
    
    def leftRotate(self, z): 
        y = z.right 
        T2 = y.left 

		
        y.left = z 
        z.right = T2 
        z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

        return y 
    
    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

		 
        y.right = z 
        z.left = T3 

        z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 
    
    #get the lowest element of the tree 
    def getMin(self,root):
        if root is None or root.left is None:
            return root
        return self.getMin(root.left)
    
    
    def UpdatePlayer(self,root,key_name,key_new_score):
        if root is None:
            return
        if root.name==key_name:
            root.val+=key_new_score
        if root.name<key_name:
            return self.UpdatePlayer(root.right,key_name,key_new_score)
        else:
            return self.UpdatePlayer(root.left,key_name,key_new_score)
            
    # almost same principle as insert method 
    def Delete(self,root,key_name):
        if not root:
            return root
        if root.name<key_name:
            return self.Delete(root.right,key_name)
        if root.name>key_name:
            return self.Delete(root.left,key_name)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMin(root.right)
            root.name = temp.name
            root.right = self.Delete(root.right,temp.name)
        #Update the tree
        
        if root is None:
            return root
        
        root.height = 1+ max(self.getHeight(root.left)
                             ,self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        if balance > 1 and key_name < root.left.name: 
            return  self.rightRotate(root) 

        if balance < -1 and key_name > root.right.name: 
            return self.leftRotate(root) 

        if balance > 1 and key_name > root.left.name: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        if balance < -1 and key_name < root.right.name: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 

        
        
    def InOrder(self, root): # print the nodes in order
        if not root: 
            return
        self.InOrder(root.left) 
        print("name : {},score : {} \n".format(root.name,root.val), end="") 
        self.InOrder(root.right)
        
    def PreOrder(self, root): # print the nodes like the Preorder pattern 
        if not root: 
            return
        self.InOrder(root.left) 
        self.InOrder(root.right)
        print("name : {},score : {} \n".format(root.name,root.val), end="") 
        
        
    def InOrder_List(self,root,res=None):#return an array of all the nodes in the Tree
        if res is None:
            res = []
        if root.left:
            res = self.InOrder_List(root.left,res)
        res+=[root]
        if root.right:
            res= self.InOrder_List(root.right,res)
        return res
        
        
        
        
        