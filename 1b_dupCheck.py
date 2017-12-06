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
    listSize = 0
    for line in f:
        line = line[:-1]
        if line != 'secquenceString':
            listSize+=1  
    hashTableSize = int(math.floor(listSize * 1.3))
    f.close()

    print 'tableSize is ', listSize

    #initialize hash table
    table = [None] * hashTableSize 
    processed = 0 

    # To-Do: Use the Sequence File Format!
    # processing the input
    with open(filename) as f:
        for line in f:
            #getting rid of line-break char \n
            line = line[:-1]
            if line != 'secquenceString':
                # calculate index by using the upper hash-function
                index = get_table_index(get_string_hash(line))
                inserted = False 
                while not inserted:
                    if table[index] == None:
                        #no collision, no duplicate -> good to go. Insert value in hash-table.
                        table[index] = line
                        inserted = True
                        processed +=1 #for visualisation
                    else:
                        #already an entry at index-position: Using linear probing:
                        #first check if it's a actual duplicate
                        if table[index] == line:
                            #handle the duplicate: for first moment just count the duplicates.
                            dupCount += 1
                            processed +=1 #for visualisation
                            inserted = True
                        else:
                            #value isn't a duplicate -> So it's another link -> set index to next position
                            colCount +=1 
                            index = (index + 1) % hashTableSize
                if (processed / float(listSize) * 100) % 10 == 0:
                    currTime = time.time()
                    #Readable version:
                    #print str(processed / float(listSize) * 100) + '% processed:\n'+ str(currTime- start)+'s elapsed.'
                    #Plotable version:
                    #print str(int(processed / float(listSize) * 100)) + '    '+ str(currTime- start)
                    #portable version 2:
                    print str(currTime- start) + '    '+  str(int(processed / float(listSize) * 100)) 
            else:
                # To-Do: handle the sequence-File-format corretly
                pass
        f.close()

    #stop time measuring
    end = time.time()

    print "collisions: " , colCount
    print "dups found: ", dupCount
    print "elapsed time: ", end-start

    #for practical use: implement something for writing data to file