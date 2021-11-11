from datetime import datetime
import random
import math

#import players here

def Setup():
    
    players =[]
    MinGame(players,900,6000)

def MinGame (players,rounds,towin): #towin is points to win the round
    matches =[]
    wins = []
    names=[]
    for p in players:               
        names.append(p.__name__)    #names are nice 
        wins.append(0)              #everyone starts with zero

    for n in range(rounds):         #each round is a separate game
        scores = MinRound(players,towin)    #play, collect scores
        matches.append(scores)              #save scores for round
        maxScore = max(scores)              
        maxIndex = scores.index(maxScore)   #find the winner
        wins[maxIndex] +=1                  #winner gets a GAME point
        Write(n,names,scores)
        
    print(wins)
    print(names)

def MinRound(players,towin):
    array = [[]]                    #construct initial array
    iterate = range(len(players))   #only range ever iterated
    roundwin = towin
    for i in iterate:
        array[0].append(0)          #array[0] is running total of scores

    while max(array[0])<roundwin:  #winning score
                                    #There can only be one.
        if array[0].count(max(array[0]))>1 and max(array[0])==roundwin :
            roundwin+=1             #change the score target
            
        move = []
        for k in iterate:
            play = players[k]       #set up player from list of players
            pick = play(array)      #call player function, get choice
            if(pick not in [0,1]):  #check for invalid choice
                pick = random.choice([0,1]) #sanitize
            move.append(pick)       #add choice to list
        array.append(move)          #add this round choices to array
        
        count = array[-1].count(1) - array[-1].count(0)
                    #neg if more zeros, pos if more ones,
                    #works if player count odd  
        minor = 0
        if count > 0 :              #determine winning choice
            minor = 1
            
        for j in iterate:           #loop over round
            if(array[-1][j] == minor):
                array[0][j] += 1    #winners get ROUND point
                  
    return array[0]                 #return list of scores

def Write(Round, names, scores):
    #CSV file with round scores
    date=datetime.now().strftime('%Y-%m-%d')   
    file=open(date+" Stats.csv" ,"a+")
    if(Round ==0):
        file.write("Round #,Score,")
        for name in names:
            file.write(str(name)+",")
        file.write("\n")
    file.write(str(Round+1)+", ,")
    for score in scores:
        file.write(str(score)+",")
    file.write("\n")
    file.close()

Setup()

