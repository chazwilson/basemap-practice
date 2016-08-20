#from mpl_toolkits.basemap import Basemap
#import numpy as np
#import matplotlib.pyplot as plt

#coordinates for osaka
osalat = 34.693738
osalon = 135.502165

#creates a map centered at osaka's longitude
#m = Basemap(projection='robin', lon_0 = osalon)

inputfile = open("coordinates.csv","r")
participants = inputfile.readlines()
#strip out new line chars (not necessary, but neat)
participants = [line.replace('\n', '') for line in participants]
#split row lists into lists of lists
participants = [line.strip().split(",") for line in participants]
coordinates = [[i[1],i[2]] for i in participants]
indcoordcount = []
indcoordinates = []
for i in coordinates:
    #this if statement ignores empty fields
    if i[0]:
        # this always doesnt work, it keeps adding i to the indcoordinates list
        # im really curious why this doesn't work
        if i not in indcoordinates:
            indcoordinates += i
            print(i)
        else:
            #ive never gotten this far...
            x = indcoordinates.index(i)
            print(str(x))
            coordcount[x] += 1

#for i in participants:
    #if i[3]:
        #partlon = float(i[4])
        #partlat = float(i[3])
        #m.drawgreatcircle(osalon,osalat,partlon,partlat,linewidth=2,color='w',alpha = 1)
    #print(partlon, partlat)


#m.drawgreatcircle(osalon,osalat,mylocation[2],mylocation[1],linewidth=1,color='r')

#m.bluemarble()

# displays map
#plt.show()

