import folium
import pandas as pd
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim

data = pd.read_csv("Geo_try/kjg-mitglieder.csv", sep=";")

geolocator = Nominatim(timeout=None)
location_list = []

for i in range(data.__len__()):
    location = geolocator.geocode(data['plz'][i])
    location_list.append((location.latitude, location.longitude))

folium_map = folium.Map(location=[51.144, 9.902],
                        zoom_start=6.5,
                        tiles="CartoDB positron")

marker_cluster = MarkerCluster().add_to(folium_map)

for point in range(0, data.__len__()):
    folium.Marker(location_list[point]).add_to(marker_cluster)

marker_cluster.save("kjg_dv_fulda_locations.html")