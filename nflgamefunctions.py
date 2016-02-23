import nflgame
from fractions import Fraction

def find_playerid(name, team=None):
    if not nflgame.find(name, team):
        return 'No match'
    if len(nflgame.find(name, team)) > 1:
        print 'Could be either {}'.format(
            ' or '.join([str(p) for p in nflgame.find(name, team)]))
        return [p.gsis_id for p in nflgame.find(name, team)]
    else:
        return nflgame.find(name, team)[0].gsis_id

def print_playerid(name, team=None):
    return find_playerid(name, team)

def getScore(player,statsList):
    playerstats=player[player.find("%")+1:]+","
    playerScore=0.0
    while (playerstats.find(":")>0):
        current_stat=playerstats[:playerstats.find(":")].strip()
        for x in statsList:

            if current_stat==x[:x.rfind("=")]:
                #from statslist
                stat_value = Fraction(x[x.rfind("=")+1:].strip())
                stat_multiplier=playerstats[playerstats.find(":")+1:playerstats.find(",")].strip()
                playerScore = playerScore+(float(stat_value)*float(stat_multiplier))

        playerstats=playerstats[playerstats.find(",")+1:]
    return playerScore



def padStats(player,statsList):
    playerstats=player[player.find("%")+1:]+","
    padded = []

    for num,stat in enumerate(statsList):

        statname=stat[:stat.find("=")]+":"

        if playerstats.find(statname)==-1:
            padded.append(0)
        else:
            statpos=playerstats.find(statname)
            temp = playerstats[playerstats.find(":",statpos)+1:playerstats.find(",",statpos)]
            #temp = playerstats[statpos:playerstats.find(":",statpos)]
            padded.append(temp.strip())

    return padded



def getFantScoring(filename):
    fantStats=open(filename,"r")
    fantScoring=[]
    for stat in fantStats:
        statName=stat[:stat.find("=")]
        statValue=stat[stat.rfind("="):]
        fantScoring.append(statName+statValue.strip())
    fantStats.close()
    return fantScoring
