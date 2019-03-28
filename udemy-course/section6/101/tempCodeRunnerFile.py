gitude'] = [arcgis.geocode(', '.join(list(df.loc[row, 'Address':'State']))).longitude for row in range(len(df))]
df['La