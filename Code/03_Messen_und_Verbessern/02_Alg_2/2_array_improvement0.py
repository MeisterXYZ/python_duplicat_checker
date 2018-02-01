import sys
import os
import time

#get input-informations:
filename = sys.argv[1]
try:
    sequenzFile = open(filename, 'r')
except IOError:
    print 'cannot open sequenz-file', filename
else:
    #initialize table
    table = []
    # for handling the Sequence File Format
    isSequenceString = False
    for uri in sequenzFile:
        #getting rid of line-break char \n
            uri = uri[:-1]
            #handling the Sequence File Format
            if uri[:9] == 'secquence':
                if uri == 'secquenceString':
                    isSequenceString = True
                else:
                    isSequenceString = False
            else:
                if not isSequenceString:
                    raise ValueError('Not all of the file-content was in "secquenceString"-format.')
                else:
                    #check if element is already in list
                    elementInList = False
                    i=0
                    while (not elementInList) and (i<len(table)):
                        if table[i] == uri:
                            elementInList = True 
                            #ignore duplicate
                        i+=1
                    #otherwise append element to list
                    if not elementInList:
                        table.append(uri)
    sequenzFile.close()
    #writing unique list to file
    # with open ('Output_array.txt' , 'w') as f:
    #     for i in table:
    #         f.write(i)
    #         f.write('\n')