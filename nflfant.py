import nflgame
import fractions
import xlwt
from formatting import formatName,getTeam,retName,retTeam,retID, retPos
from nflgamefunctions import print_playerid, getScore, getFantScoring, padStats

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


#padStats("Calais Campbell#00-0026190$ARI&DL%defense_tkl: 46, defense_ast: 15, defense_tkl_loss: 16, defense_tkl_loss_yds: 59, defense_pass_def: 2, defense_qbhit: 18, defense_sk_yds: -44, defense_sk: 5.0, penalty: 3, penalty_yds: 25, defense_tkl_primary: 1, defense_frec_yds: 0, defense_frec: 1",fantScoring)

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

outBook = xlwt.Workbook()
outSheet=outBook.add_sheet("IndivStats")
cols = ["First","Last","Team","Pos","GSIS"]
for x in fantScoring:
    cols.append(x)
row_count=1
for col, headings in enumerate(cols):
    outSheet.write(0,col,headings)
print "Outputting to Excel"
for x in team_list:
    for y in team_rosters[x]:
        row_count=row_count+1
        first = retName(y)

        last=first[first.rfind(" "):].strip()
        first=first[:first.find(" ")].strip()
        outSheet.write(row_count,0,first)
        outSheet.write(row_count,1,last)
        outSheet.write(row_count,2,y[y.find("$")+1:y.find("&")])
        outSheet.write(row_count,3,y[y.find("&")+1:y.find("%")])
        outSheet.write(row_count,4,retID(y))
        for z, statval in enumerate(padStats(y,fantScoring)):
            outSheet.write(row_count,z+5,statval)
    print x + " added to Excel."
outBook.save("toExcelPlayerStats.xls")
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
