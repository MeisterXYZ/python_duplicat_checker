import time

#read file...

#start time measuring
start = time.time()

#actual algorithm...

#stop time measuring
end = time.time()

#print it to console
elapsedTime = str(end-start)
print elapsedTime.replace('.',',')

#close file
#write output (commented out)