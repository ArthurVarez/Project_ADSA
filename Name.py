#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:23:34 2020

@author: Arthur
"""

import random
import string

#Defining voyels an consomns to create random words
voyels = "aeiouy"
cons = "".join(set(string.ascii_lowercase) - set(voyels))

#generating a name for a geme -> pattern cons/voyel/cons/voyel/conc/voyel....
def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(cons)
        else:
            word += random.choice(voyels)
    return word

#genrate an score for the games 
def generate_int():
    score = random.randint(0,12.0)
    return score

