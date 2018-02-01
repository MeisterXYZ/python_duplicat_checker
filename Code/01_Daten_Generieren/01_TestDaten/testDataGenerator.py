import sys
import random
import string
import numpy

#function for getting random links
def getRandLink(chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    linkId = ''.join(random.choice(chars) for _ in range(22))
    return 'https://open.spotify.com/track/' + linkId

#getFileLength
try:
    length = int(sys.argv[1])
except ValueError:
    print 'please use the first parameter for giving the number of entries you want'

#get dupFactor
if len(sys.argv) < 3 :
    dupFactor = random.randint(0,9)*.1
else:
    try: 
        dupFactor = float(sys.argv[2]) 
        if not (dupFactor >= 0 and dupFactor <= 1):
            raise ValueError
    except ValueError:
        print 'Please use second parameter for giving the duplicate-factor. \nFactor has to be from 0 to 1. \nIf none is given it will be seted randomly.'
#getSuffix
if len(sys.argv) == 4:
    suffix = '_'+str(sys.argv[3])
else:
    suffix = ''

#Fill List with random links
linkList=[]
for i in range(length):
    if i > 0:
        #insert a previous link as duplicate by the possibility of the given duplicate-factor
        if numpy.random.choice(range(2),p=[1-dupFactor, dupFactor]) == 1:
            linkList.append(linkList[i-1])
        else:
            linkList.append(getRandLink())
    else:
        linkList.append(getRandLink())

with open('generatedTestData'+str(length)+'_'+str(dupFactor)+'dupFac'+suffix+'.txt', 'w') as f:
    print >> f, 'secquenceString'
    #transfer every item from list in random order into output-file
    while len(linkList)>0:
        pick = random.randint(0,len(linkList)-1)
        print >> f, linkList[pick]
        linkList.pop(pick)

