import sys
import os
import time
import math

# defining the python standard hash-function --> callable as hash()
# ^ = bitwise XOR;   & = bitwise AND
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
# & = bitwise AND
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
    hashTableSize = int(math.floor(len(f.readlines()) * 1.3))
    f.close()

    #initialize hash table
    table = [None] * hashTableSize 

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
                    else:
                        #already an entry at index-position: Using linear probing:
                        #first check if it's a actual duplicate
                        if table[index] == line:
                            #handle the duplicate: for first moment just count the duplicates.
                            dupCount += 1
                            inserted = True
                        else:
                            #value isn't a duplicate -> So it's another link -> set index to next position
                            colCount +=1 
                            index = (index + 1) % hashTableSize
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