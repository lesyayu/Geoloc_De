import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.DataFrame({'PLZ': ['10115', '10247', '10318', '33100','33102','33104', '67655', '60306']})
#print(df)


# Laden der Karte von Deutschland
deutschland_karte = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
deutschland_karte = deutschland_karte[deutschland_karte['name'] == 'Germany']



# Erstellen einer Matplotlib-Figur und Achse
fig, ax = plt.subplots(figsize=(10, 10))

# Darstellung der Karte von Deutschland
deutschland_karte.plot(ax=ax, color='white', edgecolor='black')

# Setzen von Titel und Achsenbeschriftungen
ax.set_title('Karte von Deutschland', fontsize=15)
ax.set_xlabel('Längengrad', fontsize=12)
ax.set_ylabel('Breitengrad', fontsize=12)

plt.show()
