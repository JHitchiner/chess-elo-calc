#!/usr/bin/python

class Player:
    # Constructor with name and elo
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
    
    # Getters
    def getElo(self):
        return self.elo
    def getName(self):
        return self.name
    
    # Setters
    def setElo(self, newElo):
        self.elo = newElo
        return
    
    def __repr__(self):
        # String output of object for when putting into update.txt
        return "{}: {}".format(self.name, self.elo)
