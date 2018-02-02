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
        with open (sys.argv[1][:-4]+"_C.txt" , 'w') as w:        
            for line in f:
                w.write("https://open.spotify.com/track/"+line)
