import math
import random

def copybest(table):
    if len(table) <= 1:             #first move random
        return random.choice([0,1])
    best = max(table[0])            #get best score
    leader = table[0].index(best)   #get index for leader
    return table[-1][leader]        #copy leader's last move
    

def flipflop(table):
    if len(table) <= 1:             #first move random
        return random.choice([0,1])
    state = 0                       #start with 0
    for i in table[-1]:             #iterate over previous turn's moves
        state = i ^ state           #XOR with every move
    return state


def turnlist(table):
    if len(table) <= 1:
        return random.choice([0,1]) #first move random
    mod = len(table[0])             #modulus is player count
    turn = len(table)               #turn count
    return table[-1][turn%mod]      #copy last move from player #turn%mod
