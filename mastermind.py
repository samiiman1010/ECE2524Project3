#!/bin/python

print("Hello, and welcome to my interpretation of a traditional Mastermind\ngame!\nMastermind is a classic game that entails one player guessing a set\nof colors, in order, that is generated by another player.  For this version,\n I'll be the player who creates the random color sequence, and you'll have\n to guess what it is.  If you want to hear more about the rules of the game,\ntype y now; otherwise type n (don't type anything besides that...I don't\nwant to write a handler for a bad input...)\n\n")

response = input("y/n?\n")

if response == "y":
    print("Okay, so there are 8 different colors in the game: red, orange, yellow,\ngreen, blue, violet, black, and brown.  When you start the game, I will\nrandomly select a sequence of 5 colors, and some of these colors might be the same.\nYour job is to give me an initial guess on the colors I picked.\nI'll ask you for your guesses in order, because I have the colors you're guessing\norganized in a particular order that you have to match.  After you almost\ncertainly get it incorrect the first time, I'll let you know how you did; if\nyou get a correct color in a correct location, I'll let you know you'll\nguess again with a new sequence.  This process repeats until either you get it\nright or I get bored (so many 10 tries or so).  Good luck!\n\n")
