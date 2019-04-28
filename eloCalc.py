#!/usr/bin/python

KFactor = 32

def expectedScores(p1Elo, p2Elo):
    # Takes 2 players elos
    # Returns the expected scores respectivley
    q1 = 10**(p1Elo/400)
    q2 = 10**(p2Elo/400)
    es1 = q1 / (q1+q2)
    es2 = q2 / (q1+q2)
    return es1, es2

def updateElos(p1Elo, p2Elo, p1Won):
    # Takes 2 players elos and the winner (1 for p1, 0 for p2)
    # Returns the new elo values respectivley
    es1, es2 = expectedScores(p1Elo, p2Elo)
    if p1Won: #p1 Won
        p1newElo = p1Elo + KFactor*(1-es1)
        p2newElo = p2Elo + KFactor*(0-es2)
        return round(p1newElo), round(p2newElo)
    else:
        p1newElo = p1Elo + KFactor*(0-es1)
        p2newElo = p2Elo + KFactor*(1-es2)
        return round(p1newElo), round(p2newElo)
    
def setKFactor(k):
    # Takes new K Factor and sets current K Factor to it
    # Returns nothing
    KFactor = k
    return
