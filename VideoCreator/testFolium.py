import folium
import pandas as pd

mapBog = folium.Map(location=[4.657837499999999,-74.05332609999999],zoom_start=13)
mapBog.save("mabBog.html")

tooltip = "Click me!"

folium.Marker(
    [4.61560375, -74.0689023], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
).add_to(mapBog)
folium.Marker(
    [4.69059395, -74.03417855000001], popup="<b>Timberline Lodge</b>", tooltip=tooltip
).add_to(mapBog)


folium.Marker([4.61560375, -74.0689023]).add_to(mapBog)
folium.Marker([4.69059395, -74.03417855000001]).add_to(mapBog)

mapBog.save("mabBog.html")
