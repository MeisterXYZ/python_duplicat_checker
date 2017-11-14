import os
import time

######THE SEQUENTIAL ONE #1 #######
start = time.time()

#variables:
filename = "List.txt"

#helper veriables for developing:
dupCount = 0
colCount = 0

#helper vor complexity measuring
o = 0

#initialize table
table = []

with open(filename) as f:
    for line in f:
        #check if element is already in list
        elementInList = False
        for element in table:
            #this is an action raising o
            o += 1
            if element == line:
                elementInList = True
        if elementInList:
            dupCount +=1
        else:
            table.append(line)
end = time.time()

print "dups found: ", dupCount
print "o: ", o
print "elapsed time: ", end-start

for i in table:
    #print i
    pass
#implemnting something for writing it to file
