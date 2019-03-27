#!/usr/bin/python3.5
import sys
import folium
path = sys.path[0]+'/'
# print(dir(folium))

# create a map obj
f_map = folium.Map(location = [49, 36], zoom_start = 6, tiles = 'Mapbox Bright')

# create a feature group
fg = folium.FeatureGroup(name = 'My Map')

# add a marker to a feature group
fg.add_child(folium.Marker(location = [49, 36], popup = 'First marker', icon = folium.Icon(color = 'green')))
 
# add a feature group to a map
f_map.add_child(fg)

# and save map obj to a file
f_map.save(path+'Map1.html')