import sys
import os
import time
import math

# defining a function which results a index number of the table based on the inputed hash-value
# & operator stands for bitwise AND chaining
def get_table_index (hash):
    return hash & (hashTableSize - 1)

#get input-informations:
filename = sys.argv[1]
try:
    sequenzFile = open(filename, 'r')
except IOError:
    print 'cannot open sequenz-file', filename
else:
    #start time measuring
    start = time.time()

    #initialize hash table
    hashTableSize = 8
    table = [None] * hashTableSize
    processed = 0 

    # processing the input
    with open(filename) as sequenzFile:
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
                    # calculate index by using the upper hash-function
                    index = get_table_index(hash(uri))
                    inserted = False 
                    perturbation = -1
                    while not inserted:
                        if table[index] == None:
                            #no collision, no duplicate -> good to go. Insert value in hash-table.
                            table[index] = uri
                            inserted = True
                            processed +=1
                        else:
                            #already an entry at index-position: Using phyton probing:
                            #first check if it's a actual duplicate
                            if table[index] == uri:
                                #handle the duplicate: for first moment just count the duplicates.
                                processed +=1
                                inserted = True
                            else:
                                #value isn't a duplicate -> So it's another link -> set index to next position
                                if perturbation == -1:
                                    perturbation = hash(uri)
                                else:
                                    perturbation = perturbation >> 5
                                index = ((5*index)+1+perturbation) % hashTableSize
                    
                    #resize table if 2/3-Limit is passed
                    if processed > (2./3)*hashTableSize:
                        #calculate new table size
                        while not 4 * processed < hashTableSize: 
                            hashTableSize = hashTableSize * 2
                        #generate new table
                        newTable = [None] * hashTableSize
                        #transfer values from old into table
                        for i in table:
                            if i != None:
                                inserted = False
                                perturbation = -1
                                index = get_table_index(hash(i))
                                while not inserted:
                                    if newTable[index] != None:
                                        if perturbation == -1:
                                            perturbation = hash(i)
                                        else:
                                            perturbation = perturbation >> 5
                                        index = ((5*index)+1+perturbation) % hashTableSize
                                    else:
                                        newTable[index] = i
                                        inserted = True
                        #assign new table to variavle
                        table = newTable
        #stop time measuring
        end = time.time()

        sequenzFile.close()
    elapsedTime = str(end-start)
    print elapsedTime.replace('.',',')
    

    #writing unique list to file
    # with open ('Output_dictLike.txt' , 'w') as f:
    #     for i in table:
    #         if i!=None:
    #             f.write('https://open.spotify.com/track/'+i)
    #             f.write('\n')
