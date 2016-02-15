import nflgame
year=2015
player_list_fant = []
fplayer_list_fant =  open("cleanlist.txt", 'r')
for line in fplayer_list_fant   :
    player_list_fant.append(line)

print player_list_fant
