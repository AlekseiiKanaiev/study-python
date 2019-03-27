#!/usr/bin/python3.5
import sys
import folium
path = sys.path[0]+'/'
# print(dir(folium))
# help(folium.Map)

with open(path+'dir_folium.txt', 'w') as f:
    f.writelines(line+'\n' for line in dir(folium))

with open(path+'dir_folium.Map.txt', 'w') as f:
    f.writelines(line+'\n' for line in dir(folium.Map()))

help(folium.Marker)