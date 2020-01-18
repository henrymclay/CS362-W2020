# -*- coding: utf-8 -*-
"""
Edited Jan 17 2020

@author: hclay
(well not really, I'm just refactoring)
"""

import Dominion
import testUtility
#import random
#from collections import defaultdict

#playernames

player_names = testUtility.GetPlayer_Names()

#number of curses and victory cards

nC = testUtility.GetCurseNum()
nV = testUtility.GetVictoryNum()

#Define box

box = testUtility.GetBoxes()

#supply_order = testUtility.GetSupplyOrder()

supply_order = {0:['Curse','Copper','Estate','Cellar','Chapel','Moat','Silver','Chancellor','Village','Woodcutter',
               'Workshop','Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief',
               'Throne Room','Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch','Gold',
               'Adventurer','Province']}


#Pick 10 cards from box to be in the supply.

supply = testUtility.GetSupply()

#The supply always has these cards
# will be handled in above ^^^

#initialize the trash

trash = testUtility.GetTrash()

#Costruct the Player objects

players = testUtility.GetPlayerObject()

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)