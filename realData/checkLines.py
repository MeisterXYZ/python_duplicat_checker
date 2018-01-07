import sys
import os

filename = sys.argv[1]
try:
    f = open(filename, 'r')
except IOError:
    print 'cannot open', filename
else:
    lines = 0
    with open(filename) as f:
        for line in f:
            lines+=1;
print "lines:", lines
