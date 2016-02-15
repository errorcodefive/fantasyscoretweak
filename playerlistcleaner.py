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
    parse = parse[0:parse.rfind('-')-3]
    cleanlist.append(parse)

messlist.close()
messlist = open("messyrosters.txt",'r')
line=[]
for x in range (0,29):
    line.append(messlist.readline())

for i in range (0,29):
        line[i].strip()
        #token by regex using
        srch = re.split(r'\bRB\b|\bQB\b|\bWR\b|\bLB\b|\bK\b|\bDB\b|\bS\b|\bTE\b|\bDB\b|\bDL\b', line[i])
        for k in range(0,9):
            cleanlist.append(srch[k].strip())


outlist = open("cleanlist.txt",'w')
cleanlist.sort()
cleanset = Set(cleanlist)
cleanlist = cleanset
cleanlist = filter(None, cleanlist)

for x in cleanlist:
    outlist.write("%s\n" % x)
outlist.close()
