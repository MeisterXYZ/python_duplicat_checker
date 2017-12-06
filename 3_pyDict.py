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
    #initialize python dictionary which is a hash table 
    D = {} 
    # processing the input
    for line in f:
        #getting rid of line-break char \n
        line = line[:-1]
        if line != 'secquenceString':
            #using "in"-functionality
            if line not in D:
                D[line] = 1
            else:
                dupCount +=1
        else:
            # To-Do: handle the sequence-File-format corretly
            pass            
    f.close()

    #stop time measuring
    end = time.time()

    print "dups found: ", dupCount
    print "elapsed time: ", end-start

    #for practical use: implement something for writing data to file