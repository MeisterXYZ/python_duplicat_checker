import sys
import os

filename = sys.argv[1]
try:
    f = open(filename, 'r')
except IOError:
    print 'cannot open', filename
else:
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line)

with open (sys.argv[1][:-4]+"_"+sys.argv[2]+"DS.txt" , 'w') as f:
    f.write("secquenceString\n")
    for i in range(int(sys.argv[2])):
        f.write(lines[i])
    print "created "+sys.argv[1][:-4]+"_"+sys.argv[2]+"DS.txt"
        