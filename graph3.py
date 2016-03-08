import sys
from mpl_toolkits.basemap import Basemap
import csv
import matplotlib.pyplot as plt
import dateutil.parser

flghtMap = Basemap(llcrnrlon=-100.,llcrnrlat=20.,\
        urcrnrlon=20.,urcrnrlat=60.,\
        resolution='l',projection='merc',\
        lat_0=40,lon_0=-10,lat_ts=20.)

x, y = [], []
reader = csv.reader(open("flug.csv"), delimiter=",")

for line in reader:
    flight_id = line[0]
    lat = float(line[4])
    lon = float(line[5])
    alt = float(line[2]) * 0.3048 # m/foot
    #print(flight_id)
    if flight_id == "344417":
        if alt != 0:
            y.append(alt)

plt.plot(y)
plt.ylabel("altitude (m)")
plt.show()
