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
        #getting rid of line-break char \n and just use the last 22 chars
            uri = uri[-23:-1]
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
                    if uri in table:
                        #ignore duplicate
                        pass
                    else:
                        #otherwise append element to list
                        table.append(uri)
    sequenzFile.close()
    #writing unique list to file
    # with open ('Output_array.txt' , 'w') as f:
    #     for i in table:
    #         f.write('https://open.spotify.com/track/'+i)
    #         f.write('\n')