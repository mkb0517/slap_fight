#!/usr/bin/env python

import sys
import time
from random import randint
from src.player import Player
from src.art import logo    

def slap(player1, player2):
    """Determine outcome of a single slapping turn. Return descriptive string"""
    hit_points = randint(0,5)
    player2.hit_points -= hit_points
    result = player1.name + " slapped "
    result += player2.name + "; it was intense.\n"
    result += player2.name + " lost " + str(hit_points) + " hit points." 
    return result

def play_round(player, opponent):
    start = time.time()
    action = raw_input("WHAT DO YOU WANNA DO? (SLAP OR WAIT)  ")
    end = time.time()
    if end-start<1:
        if action.lower() == "slap":
            outcome = slap(player, opponent)
            print(outcome)
            print("You slapped the opponent before they could react!\n")
    else:
        if action.lower() == "slap":
            outcome = slap(player, opponent)
            print(outcome)
            outcome = slap(opponent, player)
            print(outcome)
        elif action.lower() == "wait":
            outcome = slap(opponent, player)
            print(outcome)

# Display logo
print(logo + "\n")

# Get opponent name
opponent_name = raw_input("WHO DO YOU WANNA SLAP FIGHT?  ")

# Create two player objects
player = Player("You")
opponent = Player(opponent_name)

while player.hit_points > 0 and opponent.hit_points > 0:
    play_round(player, opponent)

if player.hit_points <= 0:
    print("\n%s WALKED AWAY IN SHAME." % player.name.upper())
else:
    print("\n%s WALKED AWAY IN SHAME." % opponent.name.upper())

# Display logo again, why not?
print(logo + "\n")

