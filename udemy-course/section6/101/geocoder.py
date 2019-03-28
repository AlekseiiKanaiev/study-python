#!/usr/bin/python3.5

import pandas
from geopy.geocoders import ArcGIS

arcgis = ArcGIS()

df = pandas.read_csv('udemy-course/section6/98/supermarkets.csv')
print(df)

# longitude = []
# latitude = []

# for row in range(len(df)):
#     longitude.append(arcgis.geocode(', '.join(list(df.loc[row, 'Address':'State']))).longitude)
#     latitude.append(arcgis.geocode(', '.join(list(df.loc[row, 'Address':'State']))).latitude)

# df['Longitude'] = [arcgis.geocode(', '.join(list(df.loc[row, 'Address':'State']))).longitude for row in range(len(df))]
# df['Latitude'] = [arcgis.geocode(', '.join(list(df.loc[row, 'Address':'State']))).latitude for row in range(len(df))]

df['Longitude'] = (df['Address'] +', '+ df['City'] +', ' + df['State']).apply(arcgis.geocode).apply(lambda x: x.longitude)
df['Latitude'] = (df['Address'] +', ' + df['City'] +', ' + df['State']).apply(arcgis.geocode).apply(lambda x: x.latitude)

print(df)

