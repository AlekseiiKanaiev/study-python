#!/usr/bin/python3.5
import sys

import folium
import pandas

path = sys.path[0]+'/'

df = pandas.read_csv(path+'Volcanoes.txt')

def colorize(num):
    if num <= 1000:
        return 'green'
    elif 1000 < num <= 2000:
        return 'orange'
    elif 2000 < num <= 3000:
        return 'red'
    else:
        return 'darkviolet'
# create a map obj
f_map = folium.Map(location = [44, -110], zoom_start = 6, tiles = 'Mapbox Bright')

# create a feature group
fgv = folium.FeatureGroup(name = 'Volcanoes')

# create html string
html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s m
"""

# add a markers to a feature group
for lt, ln, n, el in zip(list(df['LAT']), list(df.LON), list(df.NAME), list(df.ELEV)):
    # create iframe for popup
    iframe = folium.IFrame(html = html%(n, n, el), width = 200, height = 100)
    # fg.add_child(
    #     folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), 
    #                 icon = folium.Icon(icon_color = colorize(el), icon = 'fa-circle', prefix = 'fa', angle = 1)))
    fgv.add_child(
        folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 5, weight = 1,
                        color = 'gray', fill = True, fill_color = colorize(el), fill_opacity = 0.7))

# add my marker with "" in popup
fgv.add_child(
        folium.Marker(location = [44, -110], popup = folium.Popup('My "good" marker', parse_html = True), 
                    icon = folium.Icon(color = 'blue')))

fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(data = open(path+'world.json', 'r' , encoding='utf-8-sig').read(), 
    style_function=lambda x: {
        'color':'gray', 
        'fillColor':
            'green' if x['properties']['POP2005'] < pow(10, 7) else
            'orange' if pow(10, 7) <= x['properties']['POP2005'] < 5*pow(10, 7) else
            'red' if 5*pow(10, 7) <= x['properties']['POP2005'] < 30*pow(10, 7) else 'darkviolet'
    }))



# add a feature group to the map
f_map.add_child(fgv)
f_map.add_child(fgp)

# add layer controller to the map. 
# important to put it affter adding layers to the map!!!
f_map.add_child(folium.LayerControl('topright'))

# and save map obj to a file
f_map.save(path+'Map1.html')
