import sys
from mpl_toolkits.basemap import Basemap
import csv
import matplotlib.pyplot as plt
import dateutil.parser

flightMap = Basemap(llcrnrlon=-100.,llcrnrlat=20.,\
        urcrnrlon=20.,urcrnrlat=60.,\
        resolution='l',projection='merc',\
        lat_0=40,lon_0=-10,lat_ts=20.)

x, y = [], []
reader = csv.reader(open("flug.csv"), delimiter=",")

for line in reader:
    flight_id = line[0]
    lat = float(line[4])
    lon = float(line[5])
    if flight_id == "344417":
        if lat != 0:
            x.append(lat)
        if lon != 0:
            y.append(lon)

tmp = []
if len(x) > len(y):
    for i in range(0, len(x) - (len(x) - len(y))):
        tmp.append(x[i])
    x = tmp


if len(y) > len(x):
    for i in range(0, len(y) - (len(y) - len(x))):
        tmp.append(y[i])
    y = tmp

#print(str(len(y)) + " " + str(len(x)))
plt.plot(x, y)
plt.ylabel("longitude")
plt.xlabel("latitude")
plt.show()
#flightMap.plot(x, y)
#plt.show()
