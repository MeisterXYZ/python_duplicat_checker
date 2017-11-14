import os
import time

######THE SIMPLE ONE#######
"""
D = {}

with open("List.txt") as f:
    for line in f:
        #print line
        D[line] =  0
    for key, val in D.iteritems():
        print key
"""

######THE OWN ONE #1 #######

start = time.time()

#variables:
filename = "List.txt"
hashTableSize = 1000

#helper veriables for developing:
colCount = 0
dupCount = 0

#helper vor complexity measuring
o = 0


# the python standard hash-function --> callable as hash()
# ^ = bitwise XOR
# & = bitwise AND
def string_hash (s):
    p = 0
    length = len(s)
    x = ord(s[p]) << 7
    while p < length:
        x = 1000003 * x ^ ord(s[p])
        p += 1
    x = x ^ length
    return x

#initialize hash table
table = []
for i in range(hashTableSize):
    #this is an operation raises o:
    o += 1
    table.insert(i,None)

with open(filename) as f:
    for line in f:
        #calculate index by using a simple hash-function
        index = string_hash(line) & (hashTableSize - 1)
        inserted = False 
        while not inserted:
            #this is an operation raises o:
            o += 1
            if table[index] == None:
                #no collision, no duplicate -> good to go. Insert value in hash-table
                table[index] = line
                inserted = True
            else:
                #already an entry: Using linear probing:
                #first check if it's a actual duplicate
                if table[index] == line:
                    #handle the duplicate
                    #for first moment: do nothing. this just creates a unique list. count the duplicates:
                    dupCount += 1
                    inserted = True
                else:
                    #else: the value in the table is neither Null nor a duplicate -> So it's another link
                    #set index to next position
                    index = (index + 1) % hashTableSize

end = time.time()

print "collisions: " , colCount
print "dups found: ", dupCount
print "o: ",o
print "elapsed time: ", end-start



for i in table:
    if i != None:
        #print i
        pass
#implemnting something for writing it to file