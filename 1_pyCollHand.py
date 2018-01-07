import sys
import os
import time
import math

# defining the python standard hash-function --> callable as hash()
# ^ operator stands for bitwise XOR chaining
# & operator stands for bitwise AND chaining
def get_string_hash (s):
    p = 0
    length = len(s)
    x = ord(s[p]) << 7
    while p < length:
        x = 1000003 * x ^ ord(s[p])
        p += 1
    x = x ^ length
    return x

# defining a function which results a index number of the table based on the inputed hash-value
# & operator stands for bitwise AND chaining
def get_table_index (hash):
    return hash & (hashTableSize - 1)

#time contingents
#t_resize = 0
#t_hashing = 0
#t_collhand = 0
#t_iniTable = 0
#t_evaluations = 0

#start time measuring
start = time.time()

#set variables:
colCount = 0
dupCount = 0

#get input-informations:
filename = sys.argv[1]
try:
    f = open(filename, 'r')
except IOError:
    print 'cannot open', filename
else:
    #initialize hash table
    #t_it_start = time.time()
    hashTableSize = 8
    table = [None] * hashTableSize
    #t_it_end = time.time()
    #t_iniTable += (t_it_end - t_it_start)
    processed = 0 

    # processing the input
    with open(filename) as f:
        # for handling the Sequence File Format
        isSequenceString = False
        for line in f:
            #t_ev_start = time.time()
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
                    # calculate index by using the upper hash-function
                    #t_h_start = time.time()
                    index = get_table_index(get_string_hash(line))
                    
                    t_h_end = time.time()
                    #t_hashing += (t_h_end - t_h_start)
                    #t_ev_start += (t_h_end - t_h_start)
                    inserted = False 
                    perturbation = -1
                    while not inserted:
                        if table[index] == None:
                            #no collision, no duplicate -> good to go. Insert value in hash-table.
                            table[index] = line
                            inserted = True
                            processed +=1
                        else:
                            #already an entry at index-position: Using phyton probing:
                            #first check if it's a actual duplicate
                            if table[index] == line:
                                #handle the duplicate: for first moment just count the duplicates.
                                dupCount += 1
                                processed +=1
                                inserted = True
                            else:
                                #value isn't a duplicate -> So it's another link -> set index to next position
                                #t_c_start = time.time()
                                colCount +=1 
                                if perturbation == -1:
                                    perturbation = hash(line)
                                else:
                                    perturbation = perturbation >> 5
                                index = ((5*index)+1+perturbation) % hashTableSize
                                #t_c_end = time.time()
                                #t_ev_start += (t_c_end - t_c_start)
                                #t_collhand += (t_c_end - t_c_start)
                    
                    #resize table if 2/3-Limit is passed
                    if processed > (2./3)*hashTableSize:
                        #t_r_start = time.time()
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
                        #t_r_end = time.time()
                        #t_ev_start += (t_r_end -t_r_start)
                        #t_resize += (t_r_end -t_r_start)
            #t_ev_end = time.time()
            #t_evaluations += (t_ev_end - t_ev_start)
        f.close()

    #stop time measuring
    end = time.time()

    #print "collisions: " , colCount
    #print "dups found: ", dupCount
    str = str(end-start)
    print str.replace('.',',')
    #print "table initialize time: ", t_iniTable
    #print "hashing time: ", t_hashing
    #print "collision handling time: ", t_collhand
    #print "resize time: ", t_resize
    #print "evaluation time: ", t_evaluations

    #print result to file
    '''
    with open ('Output_1_pyCollHand.txt' , 'w') as f:
        for i in table:
            if i != None:
                f.write(i)
                f.write('\n')
    '''