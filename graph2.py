import sys
from mpl_toolkits.basemap import Basemap
import csv
import matplotlib.pyplot as plt
import dateutil.parser
import re

flightMap = Basemap(urcrnrlon=18.3892305, urcrnrlat=49.5110697,
        llcrnrlon=-14.449637, llcrnrlat=31.294149)
flightMap.drawcoastlines()

x, y = [], []
reader = csv.reader(open("flug.csv"), delimiter=",")

for line in reader:
    flight_id = line[0]
    if line[4] != "" and line[5] != "":
        lat = float(line[4])
        lon = float(line[5])
        #print(flight_id)
        if lat != 0:
            x.append(lat)
        if lon != 0:
            y.append(lon)

flightMap.scatter(y, x)
plt.ylabel("longitude")
plt.show()
