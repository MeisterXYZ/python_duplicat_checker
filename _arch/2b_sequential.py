import sys
import os
import time

#start time measuring
start = time.time()

#set variables:
dupCount = 0

#get input-informations:
filename = sys.argv[1]
try:
    f = open(filename, 'r')
except IOError:
    print 'cannot open', filename
else:
    #initialize table
    table = []
    for line in f:
        #getting rid of line-break char \n
        line = line[:-1]
        if line != 'secquenceString':
            #check if element is already in list
            elementInList = False
            for element in table:
                if element == line:
                    elementInList = True
            if elementInList:
                dupCount +=1
            else:
                table.append(line)
        else:
            # To-Do: handle the sequence-File-format corretly
            pass
    f.close()

    #stop time measuring
    end = time.time()

    print "dups found: ", dupCount
    print "elapsed time: ", end-start

    #for practical use: implement something for writing data to file