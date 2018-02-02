import os
import sys
import time

#get input-informations:
filename = sys.argv[1]
try:
    sequenzFile = open(filename, 'r')
except IOError:
    print 'cannot open sequenz-file', filename
else:
    #start time measuring
    start = time.time()

    #initialize python dictionary which is a hash table 
    uriDict = {} 
    # processing the input
    for uri in sequenzFile:
        #getting rid of line-break char \n and just use the last 22 chars
        uri = uri[-23:-1]
        if uri != 'secquenceString':
            #using "in"-functionality
            if uri not in uriDict:
                uriDict[uri] = 1
            else:
                #ignore duplicate
                pass
        else:   
            # To-Do: handle the sequence-File-format corretly
            pass                
    #stop time measuring
    end = time.time()

    sequenzFile.close()

    elapsedTime = str(end-start)
    print elapsedTime.replace('.',',')

    #writing unique list to file
    # with open ('Output_pyDict.txt' , 'w') as outputFile:
    #     for uri in uriDict:
    #         outputFile.write('https://open.spotify.com/track/'+uri)
    #         outputFile.write('\n')