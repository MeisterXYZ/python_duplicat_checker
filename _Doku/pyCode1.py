uriDict = {}
for uri in sequenzFile:
    if uri not in uriDict:
        uriDict[uri] = 1
    else:
        #ignore duplicate
        pass