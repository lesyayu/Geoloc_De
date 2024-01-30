import pandas as pd
import geopandas

# Lesen der PLZ-Geokoordinaten-Datei. Latitude und Longitude nach PLZ: Spalten 'PLZ' 'lat' 'lng'
plz_geo_df = pd.read_csv('plz_geocoord.csv')

# Umbenennen der ersten Spalte in 'PLZ', wenn diese die Postleitzahlen repräsentiert
plz_geo_df.rename(columns={'Unnamed: 0': 'PLZ'}, inplace=True)

# Beispiel-DataFrame df, die PLZ enthält (ersetzen Sie dies durch Ihre eigene DataFrame)
df = pd.read_csv('PLZ_datei.csv')

# Zusammenführen der DataFrames anhand der PLZ
df_geo = pd.merge(df, plz_geo_df, on='PLZ', how='left')

# Die Spalten 'clicks7d' und 'br' aus 'df' in 'df_geo' übernehmen
#df_geo['clicks7d'] = df['clicks7d']
#df_geo['br'] = df['br']

# Der DataFrame 'df_geo' enthält nun die Spalten 'lat', 'lng', 'clicks7d' und 'br'
print(df_geo)


df_geo.to_csv('df_geo.csv', index=False)


# Anzeigen der resultierenden DataFrame df_geo
print(df_geo)

#gr = geopandas.read_file(geodatasets.get_path("df_geo.csv"))

import folium


# Laden des DataFrames aus der CSV-Datei
#df_geo = pd.read_csv('pfad_zur_ihrer_datei.csv')

# Erstellung einer Karte von Deutschland
# Die Koordinaten (51.1657, 10.4515) sind der geographische Mittelpunkt von Deutschland
deutschland_karte = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Hinzufügen der PLZ-Punkte zur Karte
for index, row in df_geo.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=2, # Radius des Punktes
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.2
    ).add_to(deutschland_karte)

# Speichern der Karte als HTML-Datei
deutschland_karte.save('deutschland_karte.html')
