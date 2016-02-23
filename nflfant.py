import nflgame
import fractions
import xlwt
from formatting import formatName,getTeam,retName,retTeam,retID, retPos
from nflgamefunctions import print_playerid, getScore, getFantScoring

year=2015
player_list_fant = []
formatplayer_list=[]
fplayer_list_fant =  open("cleanlist.txt", 'r')
team_list =[]
play_team_list=[]
team_rosters={}
team_games=[]

#load fantasy scoring system
fantScoring = getFantScoring("fantScoringSystem.txt")
print "Fantasy scoring system loaded."
#Only players from our transaction list and roster list are used
#Decided not to use every NFL player since many are unncessary since no one would pick them up
for line in fplayer_list_fant:
    player_list_fant.append(line.strip())
#formatplayer_list.append(formatName(line))

for x in range (0,32):
    team_list.append(nflgame.teams[x][0])

for x in team_list:
    xTeamRoster = []
    for y in player_list_fant:
        if getTeam(y)==x:

            playerInfo = formatName(y) + "#" + print_playerid(formatName(y),x)+"$"+x+"&"+retPos(y)
            xTeamRoster.append(playerInfo)
    team_rosters[x]=xTeamRoster
    print x+" roster loaded."

#yearly games combined
#kickers need play by play since kick distances are not recorded in combine

for x in team_list:
    teamGames=nflgame.games(year,home=x,away=x,kind='REG')
    teamCombined=nflgame.combine_play_stats(teamGames)
    playnum=-1
    print x+" stats loaded."
    for y in team_rosters[x]:

        playnum=playnum+1
        playerStats = teamCombined.playerid(retID(y))
        try:
            team_rosters[x][playnum]=team_rosters[x][playnum]+"%"+playerStats.formatted_stats()
            #print playerStats.formatted_stats()
        except AttributeError:
            print "No stats for "+y


#loop for on the fly changing of stats
# while True:
#     userIn=raw_input("X to exit, anything else to continue.")
#     if (userIn=="X" or userIn=="x"):
#         break
#     newfantvalues=getFantScoring("fantScoringSystem.txt")
#     for x in team_list:
#         for y in team_rosters[x]:
#
#             print retName(y)
#             print getScore(y,newfantvalues)

#used this to determine all stats that are recorded
# stat_types=set()
# for x in team_list:
#     for y in team_rosters[x]:
#         temp = y[y.find("%")+1:]+", "
#         while temp.find(":")>0:
#             stat_temp=temp[:temp.find(":")]
#             stat_types.add(stat_temp)
#             temp=temp[temp.find(",")+1:]
# statout = open("stat_types.txt","w")
# stat_types=sorted(stat_types)
# for x in stat_types:
#     statout.write("%s\n"%x.strip())




#for each player
#go through stats
#assign total numerical value
