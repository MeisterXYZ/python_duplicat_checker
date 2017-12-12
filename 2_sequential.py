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
    # for handling the Sequence File Format
    isSequenceString = False
    for line in f:
        #getting rid of line-break char \n
            line = line[:-1]
            #handling the Sequence File Format
            if line[:9] == 'secquence':
                if line == 'secquenceString':
                    isSequenceString = True
                else:
                    isSequenceString = False
            else:
                if not isSequenceString:
                    raise ValueError('Not all of the file-content was in "secquenceString"-format.')
                else:
                    #bad way
                    '''
                    #check if element is already in list
                    elementInList = False
                    i=0
                    while (not elementInList) and (i<len(table)):
                        if table[i] == line:
                            elementInList = True 
                            #if so raise duplicate counter
                            dupCount +=1
                        i+=1
                    #otherwise append element to list
                    if not elementInList:
                        table.append(line)
                    '''
                    #good way
                    #check if element is already in list
                    if line in table:
                        #if so raise duplicate counter
                        dupCount +=1
                    else:
                        #otherwise append element to list
                        table.append(line)
    f.close()

    #stop time measuring
    end = time.time()

    print "dups found: ", dupCount
    print "elapsed time: ", end-start

    #print result to file
    with open ('Output_2_sequential.txt' , 'w') as f:
        for i in table:
            if i != None:
                f.write(i)
                f.write('\n')
