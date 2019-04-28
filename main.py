#!/usr/bin/python
import sys
import eloCalc
from player import Player

# Scans a text file for chess games and updates players elos depending on outcome

# Proper text file format for parasing through (player names must be unique)...
# PLAYER1_NAME:ELO,PLAYER2_NAME:ELO,WINNING_PLAYERS_NAME
# Each line is a seperate game

# Each elo will be calculate as a per game basis, so no need to change elos if the same
# player plays multiple games

# The final result will be a txt file named updated.txt that will have each player that
# appeared in the chess games file with their new elo

unqPlayers = [] # List of player objects

def main():
    f = getFile()
    for l in f:
        # For each line in file, parse the data into seperate variables
        # Get winning player and remove the new line character
        winningPlayer = l.split(",")[2].replace("\n","")
        # Get player 1 name and elo
        p1Name = l.split(",")[0].split(":")[0]
        p1Elo = l.split(",")[0].split(":")[1]
        # Get player 2 name and elo
        p2Name = l.split(",")[1].split(":")[0]
        p2Elo = l.split(",")[1].split(":")[1]
        
        # Check induvidually if each player is in unqPlayers, if not create new objects
        if not unqPlayers: # If empty, add both
            unqPlayers.append(Player(p1Name, p1Elo))
            unqPlayers.append(Player(p2Name, p2Elo))
        else: # If not empty, check to see if they are already in there
            p1Found = False
            p2Found = False
            for p in unqPlayers: # Go through all players stored
                if p.getName() == p1Name: # If found
                    p1Found = True
                    p1Elo = p.getElo() # Change given elo to stored elo
                if p.getName() == p2Name: # If found
                    p2Found = True
                    p2Elo = p.getElo() # Change given elo to stored elo
            # Check if found, if not add them
            if not p1Found:
                unqPlayers.append(Player(p1Name, p1Elo))
            if not p2Found:
                unqPlayers.append(Player(p2Name, p2Elo))
        
        # p1 and p2 will be in unqPlayers now if they weren't before
        p1Won = False
        if p1Name == winningPlayer:
            p1Won = True
        # Update elo ratings
        p1Elo, p2Elo = eloCalc.updateElos(int(p1Elo), int(p2Elo), p1Won)
        # Find player objects and update their elos in that
        for p in unqPlayers:
            if p.getName() == p1Name:
                p.setElo(p1Elo)
            if p.getName() == p2Name:
                p.setElo(p2Elo)
    # Once finished going through file, output all player objects to updated.txt
    outputUpdatedToFile()
    f.close()
    
def getFile():
    while(True):
        # Ask user for file to be parsed
        finput = input("Enter file name (enter q to quit program): ")
        if finput == 'q': # If q, quit program
            sys.exit()
        try: # Try open file, if successful, return the file
            fileToReturn = open(finput, 'r')
            return fileToReturn
        except: # If not successful opening the file, report error and ask for input again
            print("Invalid input")
            pass

def outputUpdatedToFile():
    # Output all saved and updated player information to a txt file called updated.txt
    with open("updated.txt", "w") as f:
        for p in unqPlayers:
            print(p, file=f)
        
if __name__ == '__main__':
    main()
