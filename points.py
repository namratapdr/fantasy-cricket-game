
'''This modules calculates points for each Player in a team'''
import math
def bat(p):
    "To calculate points for a batsman"
    batscore = 0
    strike_rate = 0
    if p[2] > 0:
        #calculating the strike rate of the batsman
        strike_rate = int(p[1]/p[2] * 100)
        #Points for runs scored
        batscore += math.floor(p[1]/2)
        if p[1] > 50:
            batscore += 5
            if p[1] > 100:
                batscore += 10
        #strike rate points
        if (strike_rate > 100) :
            batscore += 4
        elif (strike_rate > 80) and (strike_rate < 100):
            batscore += 2
        #points for 4s or 6s
        if p[3] > 0:
            batscore  += 1 * p[3]
        if p[4] > 0:
            batscore  += 2 * p[4]
    #for fielding
    
    if p[9] > 0 :
        batscore += 10 * p[9]
    if p[10] > 0:
        batscore += 10 * p[10]
    if p[11] > 0:
        batscore += 10 * p[11]
    #return number of points the batsman scored
    return batscore

def bowl(p):
    "To calculate points for a bowler"
    bowlscore = 0
    #points for wickets
    bowlscore += p[8] * 10
    if p[8] >= 3 :
        bowlscore += 5
    if p[8] >= 5:
        bowlscore += 10
    #points for economy rate
    if p[5] > 0:
        overs = p[5] / 6
        economy_rate = (p[7] / overs)
        if economy_rate >= 3.5 and economy_rate <=4.5:
            bowlscore +=4
        elif economy_rate > 2  and economy_rate <=3.5:
            bowlscore += 7
        elif economy_rate <=2:
            bowlscore += 10
    #return number of points the bowler scored
    return bowlscore
