import re
from sets import Set

eof = False
cleanlist = []
messlist = open("messlist.txt",'r')
lincount = 0
playerchunk = ['','','','']
for x in range(0,338):
    for i in range(0,4):
        playerchunk[i]=messlist.readline()
    parse = playerchunk[1]

    playname = parse[0:parse.rfind('-')].strip()
    if playname.endswith("K"):
        playname=playname[:-1]+"&K"
    else:
        playname=playname[:-2]+"&"+playname[-2:]

    playteam = parse[parse.rfind('-')+1:parse.rfind('-')+5]
    cleanlist.append(playname+"$"+playteam.strip())

messlist.close()
messlist = open("messyrosters.txt",'r')
line=[]
for x in range (0,232):
    pickNo = messlist.readline()#don't need
    pickName = messlist.readline() #keep whole
    pickInfo = messlist.readline()
    pickTeam = pickInfo[pickInfo.find('-')+1:pickInfo.find('PICK')]
    pickPos = pickInfo[:pickInfo.find('-')-1]
    cleanlist.append((pickName.strip()+"&"+pickPos.strip()+"$"+pickTeam.strip()))

outlist = open("cleanlist.txt",'w')

cleanset = Set(cleanlist)

cleanlist = list(cleanset)


for x in cleanlist:
    outlist.write("%s\n" % x)
outlist.close()
